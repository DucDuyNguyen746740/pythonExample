class car:
    def __init__(self, model, make, purchase_price, sold_price, purchase_date, sold_date):
        self.model = model
        self.make = make
        self.purchase_price = purchase_price
        self.sold_price = sold_price
        self.purchase_date = purchase_date
        self.sold_date = sold_date

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.__model = model

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.__make = make

    def get_purchase_price(self):
        return self.purchase_price

    def set_purchase_price(self, purchase_price):
        self.__purchase_price = purchase_price

    def get_sold_price(self):
        return self.sold_price

    def set_sold_price(self, sold_price):
        self.__sold_price = sold_price

    def get_purchase_date(self):
        return self.purchase_date

    def set_purchase_date(self, purchase_date):
        self.__purchase_date = purchase_date

    def get_sold_date(self):
        return self.sold_date

    def set_sold_date(self, sold_date):
        self.__sold_date = sold_date

     

