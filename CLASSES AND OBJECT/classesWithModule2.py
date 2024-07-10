import classesWithModule

print(dir(classesWithModule))

demo = classesWithModule.agent('Bikash',20)
demo.health-=20
print(demo.health)
demo.info()
print('-'*30)

agent1 = classesWithModule.agent('ShaktiMan',39)
agent1.health-=39
agent1.info()
print('-'*30)

agent2 = classesWithModule.agent('Pandadhar',28)
agent2.health-=37
agent2.info()
print('-'*30)