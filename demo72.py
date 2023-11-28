class person():
    def _init_(self,name):
        print("arun")
        self.name=name
        
class student(person):
    def _init_(self,grade):
        self.grade=grade
        
    def display(self):
         print(self.name,self.grade)
        
s1=student("A")

