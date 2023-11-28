class grandpa():
    def phone(self):
        print("grandpa phone")
class dad(grandpa):
    def money(self):
        print("dads money")
class son(dad):
    def laptop(self):
        print("sons laptop")
ram=son()
ram.laptop()
ram.money()
ram.phone
d1=dad()
d1.phone() 
