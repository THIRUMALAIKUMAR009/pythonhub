class phone():
    chargertype="c-type"
    def _init_(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("price:",self.price)
        print("chargertype",self.chargertype)      

samsung=phone("samsung","10000")
samsung.display()
