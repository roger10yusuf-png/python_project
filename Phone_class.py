class Phone():
    def __init__(self,model,id,battery,storage):
        self.model = model
        self.id = id
        self.battery = battery
        self.storage = storage

    def display(self):
        print(self.model, self.id, self.battery, self.storage)

    def charging(self):
        self.battery = self.battery + 1
        print(self.battery)

    def using(self):
        self.battery = self.battery - 1
        print(self.battery)


phone1 = Phone("iphone",529,100,125)
phone1.using()
phone1.display()
phone1.charging()




        