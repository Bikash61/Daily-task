class person:

    def __init__(self):
        print("Program starts to run")

    def runs(self):
        print("Program is running")
    
p1 = person()
p1.runs()
print('-'*40)
print(p1.__init__())


#Making a game using python classes and objects

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
    

p1 = agent("Bikash",30)
p1.shooted()
p1.punched()
p1.punched()
p1.alive()
p1.info()
print('-'*50)
p2 = agent("Manish", 18)
p1.shooted()
p1.shooted()
p1.alive()
p1.info()
