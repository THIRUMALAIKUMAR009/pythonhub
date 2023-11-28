class laptop:
    def _init_(self):
        self.ram=""
        self.pricessor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)

hp=laptop()
dell=laptop()

hp.ram="8gb"
hp.processor="i5"

dell.ram="16gb"
dell.processor="i7"

hp.display()
dell.display()
