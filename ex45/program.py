# from sys import *
from owner import *
from horse import *
from stable import *

print "Hi. This program will help you to find out how much energy you horse need during one day." 
print "What is your name?"

owner = Owner()
stable = Stable()
horse = Horse()
	
owner.setName()

horse.setAttributes()

print "Do you have any more horses?"
print "yes or no"
answer = raw_input(">")
if answer == "yes":
	horse = Horse()
	horse.setAttributes()

stable.printHorsesInStable()

horse.findEnergyNeed()

