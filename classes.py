class person:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age 
        self.country = country

    def display(self):
        print(self.name, self.age, self.country )

person1 = person("Dave","13","germany")
person1.display()
person2 = person("kiara","17","America")
person2.display()
