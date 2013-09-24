# from sys import *
from owner import *
from horse import *

print "Hi. This program will help you to find out how much energy you horse need during one day." 
print "What is your name?"

owner = Owner()	
owner.setName()
horse = Horse()
horse.setAttributes()

print "%s is a %s" % (horse.name, horse.gender)