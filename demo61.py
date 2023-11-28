class laptop():
    def _init_(self):
        self.brand=""
        self.price=44
    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)


hp=laptop()
hp.setprice(20000)
hp.getprice()
