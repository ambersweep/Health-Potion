import random

#initializes starting health
health = 50

#sets the difficulty level
difficulty = 3

#initializes the health potion which is a random number between 25 and 50
potionHealth = random.randint(25,50)

#gives health its health potion and scales it with the difficulty level by dividing it by the difficulty. 
#int gets rid of decimal by changing it from a float to an integer
health = health + int(potionHealth/difficulty)
#prints result
print(health)