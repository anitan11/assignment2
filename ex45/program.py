# from sys import *
from owner import *
from horse import *
from stable import *

owner = Owner()
stable = Stable()
horse = Horse()
	
print "Hi. This program will help you to find out how much energy you horse need during one day."
print "What is your name?"

owner.setName()

horse.setAttributes()

stable.printHorsesInStable()

# horse.findEnergyNeed()

