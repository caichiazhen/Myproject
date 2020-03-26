class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__name = new_price