class Horse(object):  

	name = "None"
	hight = "None"
	type = 	"None"
	gender = "None"
	feh=0.0
	training = "light"


		#if answer == "yes":
		#	horse = Horse()
		#	horse.setAttributes()
		
	
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
		
	def findEnergyNeed(self):   #needs to be split in to several functions
	# This function uses the horses hight to find the weight. Then it checks to see if the horse in under the pony-line or not.
	# If it is not, it check to see if the type is one of the types that needs some additional energy. Then it checks to see if it is a stallion.
	# Stallions also needs some additional energy on top of the extra energy already given. Then this function calculates the extra energy for the
	# traing the horse gets. In the end it sums it all up and returns it.
		weight = self.hight * 6.25 - 625.0
		
		if self.hight >= 148:
			vfeh = weight / 100
			if type == "varmblodshest": #should do something to make sure the user spells it correctly
				vfeh = vfeh * 1.05

			elif type == "kaldblodstraver": #should do something to make sure the user spells it correctly
				vfeh = vfeh * 1.05

			elif type == "fullblodshest": #should do something to make sure the user spells it correctly
				vfeh = vfeh * 1.10

		elif self.hight < 148:
			temp = weight / 100
			vfeh = temp * 0.8	#(103,5 / 100) * 0,8 = 1,035 * 0,8 = 0,828

		if self.gender == "stallion":
			vfeh = vfeh * 1.05 # 0,828 + (0,828 * 0,05) = 0,8694
			
		if self.training == "light":
			vfeh = vfeh * 1.25	# 0,8694 * 0,25 = 0,21735
		elif self.training == "medium":
			vfeh = vfeh * 1.5
		elif self.training == "hard":
			vfeh = vfeh * 1.75
		elif self.training == "intense":
			vfeh = vfeh * 2

		vfeh = round(vfeh, 2) # 0,21735 + 0,8694 = 1,08675
		
		self.feh = vfeh
		
class Owner(object):
# A small object to hold the email-variable

	email = "None"

	def setEmail(self, email):
		self.email = email
		
	def getEmail(self):
		return self.email

