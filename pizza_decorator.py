
import abc

class Pizza(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def get_price(self):
		pass

	@abc.abstractmethod
	def get_status(self):
		pass


class Base(Pizza):
	__base = 0

	def get_price(self):
		return self.__base
	
	def get_status(self):
		return "Base"


class PizzaDecorator(Pizza):
	def __init__(self, pizza):
		self.pizza = pizza

	def get_price(self):
		return self.pizza.get_price()

	def get_status(self):
		return self.pizza.get_status()


class Big(PizzaDecorator):
	def __init__(self, pizza):
		super(Big, self).__init__(pizza)
		self.__big_dough_price = 9.0

	@property
	def price(self):
		return self.__big_dough_price

	def get_price(self):
		return super(Big, self).get_price() + self.__big_dough_price 

	def get_status(self):
		return super(Big, self).get_status() + " Big"

class Small(PizzaDecorator):
	def __init__(self, pizza):
		super(Small, self).__init__(pizza)
		self.__small_dough_price = 5.0

	@property
	def price(self):
		return self.__small_dough_price

	def get_price(self):
		return super(Small, self).get_price() + self.__small_dough_price

	def get_status(self):
		return super(Small, self).get_status() + " Small"


class Olives(PizzaDecorator):
	def __init__(self, pizza):
		super(Olives, self).__init__(pizza)
		self.__olives_price = 2.5

	@property
	def price(self):
		return self.__olives_price

	def get_price(self):
		return super(Olives, self).get_price() + self.__olives_price 

	def get_status(self):
		return super(Olives, self).get_status() + " Olives"


class Onions(PizzaDecorator):
	def __init__(self, pizza):
		super(Onions, self).__init__(pizza)
		self.__onions_price = 2.7

	@property
	def price(self):
		return self.__onions_price

	def get_price(self):
		return super(Onions, self).get_price() + self.__onions_price

	def get_status(self):
		return super(Onions, self).get_status() + " Onions"


class Tomatoes(PizzaDecorator):
	def __init__(self, pizza):
		super(Tomatoes, self).__init__(pizza)
		self.__tomatoes_price = 3.0

	@property
	def price(self):
		return self.__tomatoes_price

	def get_price(self):
		return super(Tomatoes, self).get_price() + self.__tomatoes_price 

	def get_status(self):
		return super(Tomatoes, self).get_status() + " Tomatoes"

class Pepperoni(PizzaDecorator):
	def __init__(self, pizza):
		super(Pepperoni, self).__init__(pizza)
		self.__pepperoni_price = 3.5

	@property
	def price(self):
		return self.__pepperoni_price

	def get_price(self):
		return super(Pepperoni, self).get_price() + self.__pepperoni_price 

	def get_status(self):
		return super(Pepperoni, self).get_status() + " Pepperoni"

#=========================================================================

class PizzaBuilder:
	def __init__(self, pizza_type):
		self.pizza_type = pizza_type
		self.extentions_list = []
		self.pizza = eval(pizza_type)()
		
	def add_extention(self, extention):
		self.pizza = eval(extention)(self.pizza)
		self.extentions_list.append(extention)

	def remove_extention(self, extention):
		if extention in self.extentions_list:
			self.extentions_list.remove(extention)
		
		temp_pizza = eval(self.pizza_type)()
		for ex in self.extentions_list:
			temp_pizza = eval(ex)(temp_pizza)
		
		self.pizza = temp_pizza


	def get_price(self):
		return self.pizza.get_price()

	def get_status(self):
		return self.pizza.get_status()