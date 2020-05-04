import tkinter as tk
import sqlite3
import os
import tkinter.messagebox
from PIL import ImageTk,Image
import tkinter.font as tkFont
from database import Database
from pathlib import Path
from pizza_decorator import *
import re

class window_manager(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        self.container = container
 
        self.frames = {}

        container.grid(row=0, column=0, padx=10, pady=5) 

        tple_windows = (MainPage, SignIn, SignUp)

        for F in tple_windows:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_page(MainPage)

    def show_page(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def cr_acc(self, emaill):
        framee = MyAccount(emaill, self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def create_history_frame(self, mailee):
        framee = History(mailee, self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def create_order_page_frame(self, mailee):
        framee = MakeAnOrder(mailee, self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def create_ready_pizza_page_frame(self, mailee):
        framee = MenuPizzas(mailee, self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def create_NEW(self):
        framee = NewPizza(self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def create_custom_pizza_page_frame(self, mailee):
        framee = CustomPizzas(mailee, self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def new_pizza(self):
        framee = NewPizza(self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def whole_Orders(self):
        framee = AllOrders(self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def rem_pizza(self):
        framee = RemovePizza(self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def whole_Menu(self):
        framee = WholeMenu(self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

    def create_Admin(self):
        framee = AdminAccount(self.container, self)
        framee.grid(row = 0, column = 0, sticky = "nsew")
        return framee

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label = tk.Label(self, text="MAIN PAGE", font = fontStyle)
        label.grid(row=40, column=30, padx=10, pady=5)
        self.grid_rowconfigure(0, minsize=100)
        self.grid_columnconfigure(0, minsize=50)
    
        in_button = tk.Button(self, text = "Sign in", width = 7, command = lambda: controller.show_page(SignIn))
        in_button.grid(row=45, column=30, padx=10, pady=5)
        up_button = tk.Button(self, text = "Sign up", width = 7, command = lambda: controller.show_page(SignUp))
        up_button.grid(row=50, column=30, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((300, 200), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=80, column=30, padx=10, pady=5)

class SignIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_rowconfigure(0, minsize=100)
        self.grid_columnconfigure(0, minsize=50)
        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label = tk.Label(self, text="SIGN IN", font = fontStyle)
        label.grid(row=0, column=0, padx=10, pady=5)

        mail_obj = tk.StringVar()
        mail_label = tk.Label(self, text = "E-mail")
        mail_label.grid(row=1, column=0, padx=10, pady=5)
        self.mail_entry = tk.Entry(self, textvariable = mail_obj)
        self.mail_entry.grid(row=2, column=0, padx=10, pady=5)

        password_obj = tk.StringVar() 
        password_label = tk.Label(self, text = "Password")
        password_label.grid(row=3, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self, textvariable = password_obj, show = "*")
        self.password_entry.grid(row=4, column=0, padx=10, pady=5)


        go_to_account_button = tk.Button(self, text = "Enter", width = 7, command = lambda: self.check_and_go_to_account(mail_obj, password_obj))
        go_to_account_button.grid(row=5, column=0, padx=10, pady=5)
        go_to_home_button = tk.Button(self, text = "Home", width = 7, command = lambda: controller.show_page(MainPage))
        go_to_home_button.grid(row=6, column=0, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((300, 200), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=9, column=0, padx=10, pady=5)

    def check_and_go_to_account(self, ml, passw):
        db = Database()
        x = db.check_from_db(ml, passw)

        maill = (ml.get(),)
        pasw = (passw.get(),)

        if(maill[0]!="" and pasw[0]!=""):

            if(x == True and maill[0] != "admin@gmail.com" and pasw[0] != "admin"):
                acc_frame = self.controller.cr_acc(ml.get())
                acc_frame.tkraise()
                self.mail_entry.delete(0, "end")
                self.password_entry.delete(0, "end")
            elif(x==True and maill[0] == "admin@gmail.com" and pasw[0] == "admin"):
                admin_acc_frame = self.controller.create_Admin()
                admin_acc_frame.tkraise()
                self.mail_entry.delete(0, "end")
                self.password_entry.delete(0, "end")
            else:
                tk.messagebox.showwarning(title = "Warning", message = "No such account!")
                self.mail_entry.delete(0, "end")
                self.password_entry.delete(0, "end")
        else:
            tk.messagebox.showwarning(title = "Warning", message = "All entries should be filled!")


class SignUp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.grid_rowconfigure(0, minsize=50)
        self.grid_columnconfigure(0, minsize=50)
        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label = tk.Label(self, text="SIGN UP", font = fontStyle)
        label.grid(row=0, column=0, padx=10, pady=5)

        name_obj = tk.StringVar()
        name_label = tk.Label(self, text = "Name" )
        name_label.grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self, textvariable = name_obj)
        self.name_entry.grid(row=2, column=0, padx=10, pady=5)

        sname_obj = tk.StringVar()
        sname_label = tk.Label(self, text = "Surname" )
        sname_label.grid(row=3, column=0, padx=10, pady=5)
        self.sname_entry = tk.Entry(self, textvariable = sname_obj)
        self.sname_entry.grid(row=4, column=0, padx=10, pady=5)

        email_obj = tk.StringVar()
        email_label = tk.Label(self, text = "E-mail" )
        email_label.grid(row=5, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self, textvariable = email_obj)
        self.email_entry.grid(row=6, column=0, padx=10, pady=5)

        pass_obj = tk.StringVar()
        pass_label = tk.Label(self, text = "Password" )
        pass_label.grid(row=7, column=0, padx=10, pady=5)
        self.pass_entry = tk.Entry(self, textvariable = pass_obj, show = "*")
        self.pass_entry.grid(row=8, column=0, padx=10, pady=5)

        pass_repeat_obj = tk.StringVar()
        pass_repeat_label = tk.Label(self, text = "Repeat Password" )
        pass_repeat_label.grid(row=9, column=0, padx=10, pady=5)
        self.pass_repeat_entry = tk.Entry(self, textvariable = pass_repeat_obj, show = "*")
        self.pass_repeat_entry.grid(row=10, column=0, padx=10, pady=5)

        go_to_home_button = tk.Button(self, text = "Home", width = 7, command = lambda: controller.show_page(MainPage))
        go_to_home_button.grid(row=11, column=0, padx=10, pady=5)
        go_to_account_button = tk.Button(self, text = "Enter", width = 7, command = lambda: self.check_and_go_to_Account(name_obj, sname_obj, email_obj, 
        pass_obj, pass_repeat_obj))
        go_to_account_button.grid(row=12, column=0, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((300, 200), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=14, column=0, padx=10, pady=5)


    def check_and_go_to_Account(self, name_obj, sname_obj, email_obj, pass_obj, pass_repeat_obj):
        ne = (name_obj.get(),)
        sne = (sname_obj.get(),)
        eml = (email_obj.get(),)
        pssw = (pass_obj.get(),)
        pssw_rpt = (pass_repeat_obj.get(),)
        check = re.search("^[a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]+$" ,eml[0])       #should be changed to match real-life emails
        
        if(len(ne[0])>=3 and len(sne[0])>=3 and len(eml[0])!="" and len(pssw[0])>=5 and len(pssw_rpt[0])>0):
            if(check):
                if(pass_obj.get() == pass_repeat_obj.get()):
                    db = Database()
                    result = db.check_database(email_obj)
                    del(db)
                    if(result == True):
                        db = Database()
                        db.write_to_db(name_obj, sname_obj, email_obj, pass_obj)
                        acc_frame = self.controller.cr_acc(email_obj.get()) 
                        acc_frame.tkraise()
                        self.name_entry.delete(0,"end")
                        self.sname_entry.delete(0, "end")
                        self.email_entry.delete(0, "end")
                        self.pass_entry.delete(0, "end")
                        self.pass_repeat_entry.delete(0, "end")
                    else:
                        tk.messagebox.showwarning(title = "Warning", message = "Account exists!")
                else:
                    tk.messagebox.showwarning(title = "Warning", message = "Passwords do not match!")
            else:
                tk.messagebox.showwarning(title = "Warning", message = "Email constraints:\n\tLength: 9\n\tCan contain only letters before '@'\n\tCan not contain number\n\tShould contain at least 1 letter before and after '@' and '.' !")
        else:
            tk.messagebox.showwarning(title = "Warning", message = "All entries should be filled!\nMinimum name, surname length: 3\nMinimum email length: 9\nMinimum password length: 5")
            

class MyAccount(tk.Frame):
    def __init__(self, mail, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label = tk.Label(self, text="CUSTOMER ACCOUNT", font = fontStyle)
        label.grid(row=0, column=0, padx=10, pady=5)

        db = Database()
        info_from_db = db.organize_from_db(mail)

        name = (info_from_db[0][0],)
        sname = (info_from_db[0][1],)
        label1 = tk.Label(self, text="NAME:  "+name[0])
        label1.grid(row=1, column=0, padx=10, pady=5)
        label2 = tk.Label(self, text="SURNAME:  "+sname[0])
        label2.grid(row=2, column=0, padx=10, pady=5)

        label = tk.Label(self, text="")
        label.grid(row=3, column=0, padx=10, pady=5)
    
        show_history_button = tk.Button(self, text = "Go to history", command = lambda: self.create_history_frame(mail))
        show_history_button.grid(row=4, column=0, padx=10, pady=5)
        make_order_button = tk.Button(self, text = "Make Order", command = lambda: self.create_order_pg_frame(mail))
        make_order_button.grid(row=5, column=0, padx=10, pady=5)
        sign_out_button = tk.Button(self, text = "Sign Out", command = lambda: self.destroy_account_go_MainPage())
        sign_out_button.grid(row=6, column=0, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((300, 200), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=7, column=0, padx=10, pady=5)

    def destroy_account_go_MainPage(self):
        self.destroy()
        self.controller.show_page(MainPage)
        del(self)

    def create_history_frame(self, mail):
        self.destroy()
        hist_frame = self.controller.create_history_frame(mail)
        hist_frame.tkraise()
        del(self)

    def create_order_pg_frame(self, mail):
        self.destroy()
        order_frame = self.controller.create_order_page_frame(mail)
        order_frame.tkraise()
        del(self)


class MakeAnOrder(tk.Frame):
    def __init__(self, mail, parent, controller):
        tk.Frame.__init__(self, parent)
        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label = tk.Label(self, text="MENU", font = fontStyle)
        self.controller = controller
        label.grid(row=0, column=0, padx=10, pady=5)    
        
        to_account_button = tk.Button(self, text = "My account", command = lambda: self.destroy_order_go_account(mail))
        to_account_button.grid(row=3, column=0, padx=10, pady=5)
        sign_out_button = tk.Button(self, text = "Ready Pizzas", command = lambda: self.destroy_order_go_ready_pizzas(mail))
        sign_out_button.grid(row=6, column=0, padx=10, pady=5)
        sign_out_button = tk.Button(self, text = "Custom Pizzas", command = lambda: self.destroy_order_go_custom_pizzas(mail))
        sign_out_button.grid(row=9, column=0, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((325, 225), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=12, column=0, padx=10, pady=5)

    def destroy_order_go_account(self, mail):
        self.destroy()
        account = self.controller.cr_acc(mail)
        account.tkraise()
        del(self)

    def destroy_order_go_ready_pizzas(self, mail):
        self.destroy()
        account = self.controller.create_ready_pizza_page_frame(mail)
        account.tkraise()
        del(self)

    def destroy_order_go_custom_pizzas(self, mail):
        self.destroy()
        account = self.controller.create_custom_pizza_page_frame(mail)
        account.tkraise()
        del(self)

class MenuPizzas(tk.Frame):
    def __init__(self, mailee, parent, controller):
        tk.Frame.__init__(self, parent)

        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label_1 = tk.Label(self, text="Ready Pizzas", font = fontStyle)
        label_1.grid(row=0, column=1, padx=10, pady=5)   

        label = tk.Label(self, text="**To buy, please, press the image**")
        self.controller = controller
        label.grid(row=1, column=1, padx=10, pady=5)

        db = Database()
        ready_pizzas_from_db = db.read_all_ready_pizzas()

        r = 2
        c_l = 1
        c_i = 0
        for i in range(len(ready_pizzas_from_db)):
            single_record = ready_pizzas_from_db[i]
            db_name=single_record[0]
            db_cost=str(single_record[1])
            db_path=single_record[2]

            db_path = Path(db_path)
            
            txt = db_name+"\n"+db_cost+"$"
            lbl = tk.Label(self, text = txt)

            img = ImageTk.PhotoImage(Image.open(Path(db_path)).resize((160, 130), Image.ANTIALIAS))
            panel = tk.Button(self, image = img, command = lambda db_name=db_name, db_cost=db_cost : self.submit_and_pop_up(mailee, db_name, db_cost))
            panel.image = img
            panel.grid(row = r, column = c_i, padx=10, pady=0, sticky = "nsew")
            lbl.grid(row = r, column = c_l, padx=10, pady=0, sticky = "nsew")
            if(c_i!=0 and c_i%2==0):
                c_l=1
                c_i=0
                r+=1
            else:
                c_l+=2
                c_i+=2
        
        go_to_acc = tk.Button(self, text = "Go to Account", command = lambda: self.destroy_history_go_account(mailee))
        go_to_acc.grid(row=6+r, column=0, padx=10, pady=5)

    def submit_and_pop_up(self, mailee, db_pizza_name, db_pizza_cost):
        db = Database()
        db.make_ready_pizza_order(mailee, db_pizza_name, db_pizza_cost)
        txt = "You have purchased \""+db_pizza_name+"\" for "+db_pizza_cost+"$\nYou can view account history!" 
        tk.messagebox.showwarning(title = "Order submission", message = txt)
        
    def destroy_history_go_account(self, mail):
        self.destroy()
        account = self.controller.cr_acc(mail)
        account.tkraise()
        del(self)


class CustomPizzas(tk.Frame):
    def __init__(self, mail, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.mail = mail
        fontStyle = tkFont.Font(family="Times New Roman", size=20)
        label = tk.Label(self, text="Make Your Own Pizza", font = fontStyle)
        label.grid(row=0, column=0, padx=10, pady=0, sticky = "nsew")

        db = Database()
        all_toppings = db.read_all_ready_toppings()
        self.chosen_toppings_obj = []
        self.chosen_toppings_list = []
        
        r = 1
        
        for i in range(len(all_toppings)):
            single_record = all_toppings[i]
            db_name=single_record[0]
            db_cost=str(single_record[1])
            db_path=single_record[2]
            db_path = Path(db_path)
            
            txt = db_name+"\n"+db_cost+"$"
            lbl = tk.Label(self, text = txt)
            
            img = ImageTk.PhotoImage(Image.open(Path(db_path)).resize((100, 70), Image.ANTIALIAS))
            
            panel = tk.Label(self, image = img)
            panel.image = img
            
            self.var = tk.StringVar()
            ch_button = tk.Checkbutton(self, variable=self.var, onvalue = db_name, offvalue = "")
            self.chosen_toppings_obj.append(self.var)

            panel.grid(row = r, column = 1, padx=5, pady=0, sticky = "nsew")
            lbl.grid(row = r, column = 2, padx=5, pady=0, sticky = "nsew")
            ch_button.grid(row = r, column=0, padx=5, pady=0, sticky = "nsew")
            r += 1


        go_to_acc = tk.Button(self, text = "Submit", command = lambda: self.submit())
        go_to_acc.grid(row=r+6, column=0, padx=10, pady=5)

        go_to_acc = tk.Button(self, text = "Go to Account", command = lambda: self.destroy_history_go_account())
        go_to_acc.grid(row=2+r, column=0, padx=10, pady=5)

    def destroy_order_go_custom_pizzas(self):
        self.destroy()
        account = self.controller.create_custom_pizza_page_frame(self.mail)
        account.tkraise()
        del(self)

    def submit(self):
        for item in self.chosen_toppings_obj:
            if item.get() != "":
                self.chosen_toppings_list.append(item.get())
        if(self.chosen_toppings_list):
            self.process()
            self.chosen_toppings_obj.clear()
            self.chosen_toppings_list.clear()
            self.destroy_order_go_custom_pizzas()
            txt = "Purchase submitted!" 
            tk.messagebox.showwarning(title = "Order submission", message = txt)

    def process(self):
        pizza = PizzaBuilder('Base')
        toppings_list = self.chosen_toppings_list
        for i in range(len(toppings_list)):
            pizza.add_extention(toppings_list[i])
            
        price_to_db = pizza.get_price()
        string_to_db = pizza.get_status()
        string_to_db = string_to_db[5:]
        db = Database()
        db.make_ready_pizza_order(self.mail, string_to_db, price_to_db)

    def destroy_history_go_account(self):
        self.destroy()
        account = self.controller.cr_acc(self.mail)
        account.tkraise()
        del(self)


class History(tk.Frame):
    def __init__(self, mail, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        db = Database()
        info = db.organize_from_db(mail)
        person = info[0][0]+" "+info[0][1]
        txt = "PURCHASED BY:  "+person

        fontStyle = tkFont.Font(family="Times New Roman", size=30)
        label_1 = tk.Label(self, text = "History", font = fontStyle)
        label_1.grid(row=0, column=0, padx=10, pady=5)

        label = tk.Label(self, text=txt)
        label.grid(row=2, column=0, padx=10, pady=5)


        mylist = tk.Listbox(self)
        mylist.grid(row=3, column=0, padx=10, pady=5)


        scrollbar_v = tk.Scrollbar(self, orient=tk.VERTICAL, command = mylist.yview)
        scrollbar_v.grid(row=3, column=1, padx=10, pady=5, sticky=tk.NS)
        mylist.config(yscrollcommand = scrollbar_v.set)

        scrollbar_h = tk.Scrollbar(self, orient=tk.HORIZONTAL, command = mylist.xview)
        scrollbar_h.grid(row=4, column=0, padx=10, pady=5, sticky=tk.EW)
        mylist.config(xscrollcommand = scrollbar_h.set)

        history_ids = db.get_all_ids(mail)
        orders_by_id = db.get_orders_by_id(history_ids)
        
        
        counter = 1
        for key, value in orders_by_id.items():
            txt = str(counter)+".  *Order*: "+value+"\n\t*Date*: "+str(key)
            mylist.insert(tk.END, txt)
            counter += 1

        go_to_acc = tk.Button(self, text = "Go to Account", command = lambda: self.destroy_history_go_account(mail))
        go_to_acc.grid(row=5, column=0, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((300, 200), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=7, column=0, padx=10, pady=5)
        
    def destroy_history_go_account(self, mail):
        self.destroy()
        account = self.controller.cr_acc(mail)
        account.tkraise()
        del(self)


class AdminAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label = tk.Label(self, text="Admin Account", font = fontStyle)
        label.grid(row=0, column=0, padx=10, pady=5)
    
        add_pizza_button = tk.Button(self, text = "Add Pizza", command = self.add_pizza_page)
        add_pizza_button.grid(row=2, column=0, padx=10, pady=5)
        rm_pizza_button = tk.Button(self, text = "Remove Pizza", command = self.remove_pizza_page)
        rm_pizza_button.grid(row=3, column=0, padx=10, pady=5)
 
        view_pizzas = tk.Button(self, text = "View Whole Menu", command = self.whole_menu_page)
        view_pizzas.grid(row=4, column=0, padx=10, pady=5)

        view_pizzas = tk.Button(self, text = "View All Orders", command = self.destroy_account_go_AllOrders)
        view_pizzas.grid(row=5, column=0, padx=10, pady=5)

        view_pizzas = tk.Button(self, text = "Sign Out", command = self.destroy_account_go_MainPage)
        view_pizzas.grid(row=6, column=0, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((300, 200), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=8, column=0, padx=10, pady=5)


    def whole_menu_page(self):
        self.destroy()
        account = self.controller.whole_Menu()
        account.tkraise()
        del(self)

    def destroy_account_go_AllOrders(self):
        self.destroy()
        account = self.controller.whole_Orders()
        account.tkraise()
        del(self)

    def destroy_account_go_MainPage(self):
        self.destroy()
        self.controller.show_page(MainPage)
        del(self)

    def add_pizza_page(self):
        self.destroy()
        account = self.controller.new_pizza()
        account.tkraise()
        del(self)

    def remove_pizza_page(self):
        self.destroy()
        account = self.controller.rem_pizza()
        account.tkraise()
        del(self)

class AllOrders(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fontStyle = tkFont.Font(family="Times New Roman", size=30)
        label = tk.Label(self, text="ALL ORDERS", font = fontStyle)
        label.grid(row=0, column=0, padx=10, pady=5)
        
        db = Database()
        string_to_listbox = db.get_all_orders()

        mylist = tk.Listbox(self)
        mylist.grid(row=3, column=0, padx=10, pady=5)


        scrollbar_v = tk.Scrollbar(self, orient=tk.VERTICAL, command = mylist.yview)
        scrollbar_v.grid(row=3, column=1, padx=10, pady=5, sticky=tk.NS)
        mylist.config(yscrollcommand = scrollbar_v.set)

        scrollbar_h = tk.Scrollbar(self, orient=tk.HORIZONTAL, command = mylist.xview)
        scrollbar_h.grid(row=4, column=0, padx=10, pady=5, sticky=tk.EW)
        mylist.config(xscrollcommand = scrollbar_h.set)
        
        counter = 1
        for key, value in string_to_listbox.items():
            mylist.insert(tk.END, str(counter)+". "+value)
            counter += 1

        go_to_acc = tk.Button(self, text = "Go to Account", command = lambda: self.destroy_page_go_admin_account())
        go_to_acc.grid(row=5, column=0, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((300, 200), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=7, column=0, padx=10, pady=5)

    def destroy_page_go_admin_account(self):
        self.destroy()
        account = self.controller.create_Admin()
        account.tkraise()
        del(self)


class RemovePizza(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        fontStyle = tkFont.Font(family="Times New Roman", size=35)
        label_1 = tk.Label(self, text="Remove Pizza", font = fontStyle)
        label_1.grid(row=0, column=1, padx=10, pady=5)   
        
        label = tk.Label(self, text="**To remove, please, press the image**")
        label.grid(row=1, column=1, padx=10, pady=5)

        db = Database()
        ready_pizzas_from_db = db.read_all_ready_pizzas()

        r = 2
        c_i = 0
        c_l = 1
        for i in range(len(ready_pizzas_from_db)):
            single_record = ready_pizzas_from_db[i]
            db_name=single_record[0]
            db_cost=single_record[1]
            db_path=single_record[2]

            db_path = Path(db_path)
            
            txt = db_name+"\n"+str(db_cost)+"$"
            lbl = tk.Label(self, text = txt)

            img = ImageTk.PhotoImage(Image.open(Path(db_path)).resize((160, 130), Image.ANTIALIAS))
            panel = tk.Button(self, image = img, command = lambda db_name=db_name: self.remove_and_pop_up(db_name))
            panel.image = img

            panel.grid(row = r, column = c_i, padx=10, pady=0, sticky = "nsew")
            lbl.grid(row = r, column = c_l, padx=10, pady=0, sticky = "nsew")
            if(c_i!=0 and c_i%2==0):
                c_l=1
                c_i=0
                r+=1
            else:
                c_l+=2
                c_i+=2
        
        go_to_acc = tk.Button(self, text = "Go to Account", command = lambda: self.destroy_page_go_admin_account())
        go_to_acc.grid(row=3+r, column=0, padx=10, pady=5)

    def destroy_page_go_admin_account(self):
        self.destroy()
        account = self.controller.create_Admin()
        account.tkraise()
        del(self)

    def remove_and_pop_up(self, p_name):
        db = Database()
        db.delete_pizza(p_name)
        txt = "\""+p_name+"\" has been removed from database!"
        tk.messagebox.showwarning(title = "Submission", message = txt)


class WholeMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label = tk.Label(self, text="WHOLE MENU", font = fontStyle)
        label.grid(row=0, column=0, padx=10, pady=5)

        db = Database()
        pizza_list = db.read_all_ready_pizzas()
        toppings_list = db.read_all_ready_toppings()

        r = 2

        pizza_label = tk.Label(self, text = "--- Available Pizzas ---" )
        pizza_label.grid(row=2, column=0, padx=10, pady=5)

        for i in range(len(pizza_list)):
            pizza_name = pizza_list[i][0]
            pizza_cost = round(pizza_list[i][1], 3)

            txt = str(i+1) + ". " + pizza_name + "  -  " + str(pizza_cost) + "$"
            one_pizza_info = tk.Label(self, text = txt)
            one_pizza_info.grid(row=r+i+1, column=0, padx=10, pady=5)
            r += 1

        topping_label = tk.Label(self, text = "--- Available Toppings ---" )
        topping_label.grid(row=r+6, column=0, padx=10, pady=5)

        for j in range(len(toppings_list)):
            topping_name = toppings_list[j][0]
            topping_cost = round(toppings_list[j][1], 3)

            txt = str(j+1) + ". " + topping_name + "  -  " + str(topping_cost) + "$"
            one_topping_info = tk.Label(self, text = txt)
            one_topping_info.grid(row=r+j+7, column=0, padx=10, pady=5)
            r += 1

        acc_button = tk.Button(self, text = "Go to Account", command = lambda: self.destroy_page_go_admin_account())
        acc_button.grid(row=r+12, column=0, padx=10, pady=5)

        dir_name = os.path.dirname(os.path.abspath(__file__))
        path_img = dir_name+"/logo.png"
        img = ImageTk.PhotoImage(Image.open(Path(path_img)).resize((300, 200), Image.ANTIALIAS))
        ph_label = tk.Label(self, image = img)
        ph_label.image = img
        ph_label.grid(row=r+14, column=0, padx=10, pady=5)

    def destroy_page_go_admin_account(self):
        self.destroy()
        account = self.controller.create_Admin()
        account.tkraise()
        del(self)


class NewPizza(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        fontStyle = tkFont.Font(family="Times New Roman", size=40)
        label = tk.Label(self, text="\tAdd New Pizza Data", font = fontStyle)
        label.grid(row=0, column=0, padx=10, pady=5)

        name_label = tk.Label(self, text = "Pizza Name: " )
        name_label.grid(row=1, column=0, padx=10, pady=5)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        path_label = tk.Label(self, text = "Pizza Image Path: \n*Please, enter absolute path of .png file" )
        path_label.grid(row=2, column=0, padx=10, pady=5)

        self.path_entry = tk.Entry(self)
        self.path_entry.grid(row=2, column=1, padx=10, pady=5)

        db = Database()
        all_toppings = db.read_all_ready_toppings()
        self.chosen_toppings_obj = []
        self.chosen_toppings_list = []
        
        r = 3
        
        for i in range(len(all_toppings)):
            single_record = all_toppings[i]
            db_name=single_record[0]
            db_cost=str(single_record[1])
            db_path=single_record[2]
            db_path = Path(db_path)
            
            txt = db_name+"\n"+db_cost
            lbl = tk.Label(self, text = txt)
            
            img = ImageTk.PhotoImage(Image.open(Path(db_path)).resize((100, 70), Image.ANTIALIAS))
            
            panel = tk.Label(self, image = img)
            panel.image = img
            
            self.var = tk.StringVar()
            ch_button = tk.Checkbutton(self, variable=self.var, onvalue = db_name, offvalue = "")
            self.chosen_toppings_obj.append(self.var)

            panel.grid(row = r, column = 1, padx=5, pady=0, sticky = "nsew")
            lbl.grid(row = r, column = 2, padx=5, pady=0, sticky = "nsew")
            ch_button.grid(row = r, column=0, padx=5, pady=0, sticky = "nsew")
            r += 1


        go_to_acc = tk.Button(self, text = "Submit", command = lambda: self.submitpz())
        go_to_acc.grid(row=r+6, column=0, padx=10, pady=5)

        go_to_acc = tk.Button(self, text = "Go to Account", command = lambda: self.destroy_page_go_admin_account())
        go_to_acc.grid(row=2+r, column=0, padx=10, pady=5)


    def destroy_page_go_admin_account(self):
        self.destroy()
        account = self.controller.create_Admin()
        account.tkraise()
        del(self)


    def submitpz(self):
        for item in self.chosen_toppings_obj:
            if item.get() != "":
                self.chosen_toppings_list.append(item.get())
        if(self.chosen_toppings_list):
            self.process()
            self.chosen_toppings_obj.clear()
            self.chosen_toppings_list.clear()
            self.destroy_page_go_add_pizzas()
            txt = "Pizza has been added!" 
            tk.messagebox.showwarning(title = "Order submission", message = txt)

    def destroy_page_go_add_pizzas(self):
        self.destroy()
        account = self.controller.create_NEW()
        account.tkraise()
        del(self)

    def process(self):
        pizza = PizzaBuilder('Base')
        toppings_list = self.chosen_toppings_list
        for i in range(len(toppings_list)):
            pizza.add_extention(toppings_list[i])
            
        price_to_db = pizza.get_price()
        string_to_db = pizza.get_status()
        string_to_db = string_to_db[5:]
        name = self.name_entry.get()+" - "+string_to_db
        db = Database()
        db.add_pizza(name, price_to_db, self.path_entry.get())

def main():
    datab = Database()
    datab.create()

    app = window_manager()
    app.mainloop()

if __name__ == "__main__":
    main()
