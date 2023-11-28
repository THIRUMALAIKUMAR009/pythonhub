class animal():
    def sound(self):
        print("animal make sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class birds(animal):
    def sound(self):
        print("birds sings")
d1=dog()
d1.sound()

b1=birds()
b1.sound()
