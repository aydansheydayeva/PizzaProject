import sqlite3
import os
import random
from pathlib import Path
from datetime import datetime

class Database:
    def __init__(self):
        pass
    
    def create(self):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        con = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS 
                        users(name text, 
                            surname text, 
                            email text, 
                            password text)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS 
                        orders_users(email text, 
                                    order_id integer)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS 
                        orders(order_id integer,
                                ordered_list text,
                                cost real,
                                date_time text)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS 
                        pizzas(name text,
                            cost real,  
                            path text)""")
        
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                        toppings(name text, 
                            cost real,
                            path text)""")
        
        con.commit()
        
        admin_account_info = [("Admin", "Admin", "admin@gmail.com", "admin")]
        x = self.check_from_db_2("admin@gmail.com", "admin")
        if(x == False):
            cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", admin_account_info)
        
        con.commit()

        path = dir_name + "/menu/pizzas/Pepperoni.png"
        self.add_pizza("Pepperoni - Big Tomatoes Pepperoni", "15.50", path)

        path2 = dir_name + "/menu/pizzas/Mexicano.png"
        self.add_pizza("Mexicano - Small Onions Tomatoes", "10.70", path2)

        path3 = dir_name + "/menu/pizzas/Margarita.png"
        self.add_pizza("Margherita - Big Tomatoes Olives", "14.50", path3)
        #########################################
        
        path = dir_name + "/menu/toppings/pizza_small.png"
        self.add_topping("Small", "5.00", path)
        
        path = dir_name + "/menu/toppings/pizza_big.png"
        self.add_topping("Big", "9.00", path)
        
        path = dir_name + "/menu/toppings/olives.png"
        self.add_topping("Olives", "2.50", path)

        path = dir_name + "/menu/toppings/onions.png"
        self.add_topping("Onions", "2.70", path)

        path = dir_name + "/menu/toppings/tomatoes.png"
        self.add_topping("Tomatoes", "3.00", path)

        path = dir_name + "/menu/toppings/pepperoni.png"
        self.add_topping("Pepperoni", "3.50", path)
        
        cur.close()
        con.close()

    def delete_pizza(self, p_name):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        to_delete=[(p_name)]
        cur.execute("DELETE FROM pizzas WHERE name = (?)", to_delete)

        conn.commit()
    
        cur.close()
        conn.close()

    def add_topping(self, top_name, top_cost, top_path):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        topping = [(top_name, float(top_cost), top_path)]
        res = self.check_topping(top_name, top_cost, top_path)
        if(res == False):
            cur.executemany("INSERT INTO toppings VALUES (?, ?, ?)", topping)
        conn.commit()
    
        cur.close()
        conn.close()

    def check_topping(self, top_name, top_cost, top_path):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        top_name = (top_name,)

        top_info = tuple(cur.execute("""SELECT name, cost, path FROM toppings WHERE name = ?""", top_name))

        conn.commit()
        
        if(top_info and top_info[0][0] == top_name[0]):
            return True
        else:
            return False

        cur.close()
        conn.close()

    def read_all_ready_toppings(self):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        toppings = cur.execute("""SELECT * FROM toppings""")
        
        conn.commit()
        result = toppings.fetchall()
        cur.close()
        conn.close()
        return result

    def get_all_orders(self):
        all_orders = {}
        all_orders_new = {}

        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        orders = cur.execute("""SELECT * FROM orders""")
        result = orders.fetchall()
        conn.commit()

        for i in range(len(result)):
            all_orders[result[i][0]] = "*Order*: "+result[i][1]+" *Cost*: "+str(round(result[i][2],3))+"$"+" *Date*: "+result[i][3]     
        
        counter = 0
        for key, value in all_orders.items():
            ID = (key,)
            info = tuple(cur.execute("""SELECT email FROM orders_users WHERE order_id = ?""", ID))
            all_orders_new[counter] = "*Buyer*:"+info[0][0]+" "+value
            counter+=1

        conn.commit()
        cur.close()
        conn.close()
        return all_orders_new

    def get_all_ids(self, mail):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        mail = (mail,)
        result = cur.execute("""SELECT order_id FROM orders_users WHERE email=?""", mail)
        
        conn.commit()
        order_ids = result.fetchall()
        cur.close()
        conn.close()
        return order_ids

    def get_orders_by_id(self, list_of_tuple_ids):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        time_order_dict_to_return={}

        for i in range(len(list_of_tuple_ids)):
            id = list_of_tuple_ids[i][0]
            id = (id,)
            res = cur.execute("""SELECT ordered_list, date_time, cost FROM orders WHERE order_id = ?""", id)
            result = res.fetchone()
            costt = str(round(result[2], 3))
            time_order_dict_to_return[result[1]]=result[0]+"\n *Cost*: "+costt+"$"
        conn.commit()
        cur.close()
        conn.close()

        return time_order_dict_to_return


    def make_ready_pizza_order(self, emaill, pizza_db_name, pizza_db_cost):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        OrderID = random.randint(0, 999999999999999999)

        orders_users_info = [(emaill, OrderID)]
        cur.executemany("INSERT INTO orders_users VALUES (?, ?)", orders_users_info)
        conn.commit()

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        orders_info = [(OrderID, pizza_db_name, pizza_db_cost, dt_string)]
        cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders_info)
        conn.commit()

        cur.close()
        conn.close()


    def read_all_ready_pizzas(self):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        pizzas = cur.execute("""SELECT * FROM pizzas""")
        
        conn.commit()
        result = pizzas.fetchall()
        cur.close()
        conn.close()
        return result

    def add_pizza(self, name, cost_str, path):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        pizza = [(name, float(cost_str), path)]
        res = self.check_pizza(name, cost_str, path)
        if(res == False):
            cur.executemany("INSERT INTO pizzas VALUES (?, ?, ?)", pizza)
        conn.commit()
    
        cur.close()
        conn.close()

    def check_pizza(self, name, cost_str, path):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        name = (name,)

        pizza_info = tuple(cur.execute("""SELECT name, cost, path FROM pizzas WHERE name = ?""", name))

        conn.commit()
        
        if(pizza_info and pizza_info[0][0] == name[0]):
            return True
        else:
            return False

        cur.close()
        conn.close()


    def check_from_db_2(self, maill, passw):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        maill = (maill,)
        passw = (passw,)

        row_email_passw = tuple(cur.execute("""SELECT email, password FROM users WHERE email = ?""", maill))

        conn.commit()
        
        if(row_email_passw and row_email_passw[0][0] == maill[0] and row_email_passw[0][1] == passw[0]):
            return True
        else:
            return False

        cur.close()
        conn.close()

    def check_from_db(self, maill, passw):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = conn.cursor()

        ml = (maill.get(),)
        pasw = (passw.get(),)

        row_email_passw = tuple(cur.execute("""SELECT email, password FROM users WHERE email = ?""", ml))

        conn.commit()
        
        if(row_email_passw and row_email_passw[0][0] == ml[0] and row_email_passw[0][1] == pasw[0]):
            return True
        else:
            return False

        cur.close()
        conn.close()

    def check_database(self, email_obj):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        con = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = con.cursor()
        
        email = (email_obj.get(),)

        mail_from_db = tuple(cur.execute("""SELECT email FROM users WHERE email = ?""", email))

        if(not mail_from_db):
            return True
        else:
            return False

        con.commit()

        cur.close()
        con.close()

    def write_to_db(self, name_obj, sname_obj, email_obj, pass_obj):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        con = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = con.cursor()

        name = (name_obj.get(),)
        surname = (sname_obj.get(),)
        email = (email_obj.get(),)
        password = (pass_obj.get(),)

        user = [(name[0], surname[0], email[0], password[0])]
        cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", user)

        con.commit()

        cur.close()
        con.close()

    def organize_from_db(self, mail):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        con = sqlite3.connect(Path(dir_name + "/database.db"))
        cur = con.cursor()

        email = (mail,)

        info_from_db = tuple(cur.execute("""SELECT name, surname FROM users WHERE email = ?""", email))
        
        con.commit()

        cur.close()
        con.close()

        return info_from_db