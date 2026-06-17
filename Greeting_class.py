class Greeting():
    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

    def display_welcome(self):
        print("Welcome", self.name)

    def display_congrats(self):
        print("Congratulation", self.name+"!!")

student1 = Greeting("Roger")
student1.display_welcome()

student2 = Greeting("George")
student2.display_congrats()