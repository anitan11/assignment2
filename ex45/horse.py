from stable import *

class Horse(object):

	name = "None"
	hight = "None"
	type = 	"None"
	gender = "None"
	feh = 0.0
	training = "light"
	weight = None
	
	# The following functions is simple set- and get-functions for the global variables inside this class
	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name
		
	def setHight(self, hight): 
		self.hight = float(hight.replace(',', '.'))
		
	def getHight(self):
		return self.hight
		
	def setType(self, type):
		self.type = type

	def getType(self):
		return self.type
	
	def setGender(self, gender):
		self.gender = gender
		
	def getGender(self):
		return self.gender
		
	def setTraining(self, training):
		self.training = training
		
	def getFeh(self):
		return self.feh
		
	def setWeight(self, weight):
		self.weight = float(weight.replace(',', '.'))
		
	def findEnergyNeed(self):   #could be split in to several functions
	# This function uses the horses wight and hight to find the daily energy need. It checks to see if the horse in under the pony-line or not.
	# If it is not, it check to see if the type is one of the types that needs some additional energy. Then it checks to see if it is a stallion.
	# Stallions also needs some additional energy on top of the extra energy already given. Then this function calculates the extra energy for the
	# traing the horse gets. In the end it sums it all up and returns it.
		
		if self.hight >= 148:
			vfeh = self.weight / 100.0
			if type == "varmblodshest": #should do something to make sure the user spells it correctly
				vfeh = vfeh * 1.05

			elif type == "kaldblodstraver": #should do something to make sure the user spells it correctly
				vfeh = vfeh * 1.05

			elif type == "fullblodshest": #should do something to make sure the user spells it correctly
				vfeh = vfeh * 1.10

		elif self.hight < 148:
			temp = self.weight / 100.0
			vfeh = temp * 0.8

		if self.gender == "stallion":
			vfeh = vfeh * 1.05
			
		if self.training == "light":
			vfeh = vfeh * 1.25
		elif self.training == "medium":
			vfeh = vfeh * 1.5
		elif self.training == "hard":
			vfeh = vfeh * 1.75
		elif self.training == "intense":
			vfeh = vfeh * 2

		vfeh = round(vfeh, 2)
		
		self.feh = vfeh