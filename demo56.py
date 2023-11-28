class student:
    def _init_(self):
        self.name="suresh"
        self.regno="142219205101"
    def display(self):
        print("Name",self.name)
        print("Reg No",self.regno)

s1=student()
s2=student()

s1.name="arun"
s1.regno="1"

s2.name="suresh"
s2.regno="2"

print(s2.name)
print(s2.regno)

s1.display()
s2.display()
