class employee():
    def _init_(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def _init_(self,department):
        self.department=department

    def display(self):
        print(self.name/self.salary,self.department)

m1=manager("cse")
m1.display()
