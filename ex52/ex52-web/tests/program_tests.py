from nose.tools import *
from bin.app import app

def setup(): #load with a fresh dataset
    print "SETUP!"

def teardown(): #cleanup afterwards
    print "TEAR DOWN!"

def hook(): #It is a good idea to implement a hook that runs all tests before pushing code to a shared repository.
	pass
	
def test_basic():
    print "I RAN!"
	
	
--------------------------
horse = Horse()

def setTestVariablesOne():
	name = "X-Ellent"
	hight = "103.5"
	type = 	"shetlandspony"
	gender = "stallion"
	training = "light"
	weight = 250
	
def setTestVariablesTwo():
	horse = Horse()
	name = "Donald"
	hight = "159"
	type = 	"kaldblodstraver"
	gender = "gelding"
	training = "medium"
	weight = 500

def test_findEnergyNeed():
	setTestVariablesOne()
	feh = horse.findEnergyNeed()
	print feh
	
def test_setHorseVariables():
	setTestVariablesOne()
	horse.setHorseVariables(horsename, type, gender, training, hight, horse, weight)
	print horsename, type, gender, training, higth, horse, weight
	
def test_addMoreHorses():
	addHorse = raw_input('yes or no -->')
	
	while addHorse = 'yes'
		setTestVariablesTwo()
		addHorse = raw_input('yes or no -->')
	
	for horse in stalls
		print horse.name, horse.type, horse.gender
	
	