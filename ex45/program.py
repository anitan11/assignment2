# from sys import *
from owner import *
from horse import *

owner = Owner()
stalls = []

def run(self):
	
	print "Hi. This program will help you to find out how much energy you horse need during one day."
	print "what is your e-mail?"
	owner.setEmail(raw_input('-->'))
	
	self.setHorseVariables()
	
	for horse in stalls:
		horsename = horse.getName()
		type = horse.getType()
		gender = horse.getGender()
		feh=horse.getFeh()
		print "%s is a %s %s and therefore needs %s feh per day." % (horsename, type, gender, feh)
		print "This information could in the future be sent to %s" %(owner.getEmail())
		
	print "Start over?"
	startover = raw_input('-->')
			
	if startover == yes:
		del stalls[:]
		run()
	
def setHorseVariables(self):
# This function is responsible for setting variables in the horse object, and also put the horse object in the stalls-list.
	horse = Horse()
	print "What is your horse's name?"
	horse.setName(raw_input('-->'))
	print "What is the type of your horse?"
	horse.setType(raw_input('-->'))
	print "What is the gender of your horse? stallion, gelding or mare"
	horse.setGender(raw_input('-->'))
	print "How much do you train your horse? light, medium, hard or intense"
	horse.setTraining(raw_input('-->'))
	print "How high is you horse? - in cm"
	horse.setHight(raw_input('-->'))
	print "How much does your horse weigh? - in kg"
	horse.setWeight(raw_input('-->'))
	horse.findEnergyNeed()	#calculates the energy need for the horse
	stalls.append(horse) #saves entered horse in stable
	print "Do you have any more horses? yes or no"
	morehorses = raw_input('-->')
	
	if morehorses == yes
		setHorseVariables()
	
run()
	
			
				
		

	