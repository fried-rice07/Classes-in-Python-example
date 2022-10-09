class Object():
    def __init__(self):
        self.name = "Marcel"
    def intro(self):
        print(f"{self.name}")
call = Object()
call.intro()


class Robot():
    def introduce(self):
        print("My name " + self.name)
r1 = Robot()
r1.name = "Marcel"
r1.introduce()
