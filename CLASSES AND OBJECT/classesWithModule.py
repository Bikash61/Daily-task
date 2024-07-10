class agent:
    def __init__(self,name,age):
        print("Welcome you in the game")

        self.name = name 
        self.age = age
        self.health = 100
    
    def punched(self):
        self.health -=10
        print("Agent has been Punched")

    def shooted(self):
        self.health -=50
        print("Agent has been shooted")
    
    def alive(self):
        if self.health >0:
            print("Agent is alive")
    
    def info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Health: ", self.health)


