class goa:
    name=""
    drink=""
    def party(self):
        print("Lets party...")
    def beach(self):
        print("ENJOYING THE BEACH")

ramesh= goa()
suresh= goa()

ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print("drink:",ramesh.drink)
print(suresh.name)
print("drink:",suresh.drink)

ramesh.party()
suresh.beach()
