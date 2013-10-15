class Horse(object):  

	name = "None"
	hight = "None"
	type = 	"None"
	gender = "None"
	feh=0
	training = "light"


		#if answer == "yes":
		#	horse = Horse()
		#	horse.setAttributes()
		
	
	# The following functions is simple set- and get-functions for theg global variables inside this class
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
		
	def putHorseInStable(self):
	# Puts this horse inside an array in a stable-object
		self.stable = Stable()
		self.stable.stalls.append(self)
		
	def findEnergyNeed(self):   #needs to be split in to several functions
	# This function uses the horses hight to find the weight. Then it checks to see if the horse in under the pony-line or not.
	# If it is not, it check to see if the type is one of the types that needs some additional energy. Then it checks to see if it is a stallion.
	# Stallions also needs some additional energy on top of the extra energy already given. Then this function calculates the extra energy for the
	# traing the horse gets. In the end it sums it all up and returns it.
		weight = self.hight * 6.25 - 625.0
		
		if self.hight > 148:
			vfeh = weight // 100
			if type == "varmblodshest": #should do something to make sure the user spells it correctly
				temp = vfeh * 0.05
				vfeh = vfeh + temp
			elif type == "kaldblodstraver": #should do something to make sure the user spells it correctly
				temp = vfeh * 0.05
				vfeh = vfeh + temp
			elif type == "fullblodshest": #should do something to make sure the user spells it correctly
				temp = vfeh * 0.10
				vfeh = vfeh + temp
		elif self.hight < 148:
			temp = self.weight / 100
			vfeh = temp * 0.8

		if gender == "stallion":
			temp = vfeh * 0.05
			vfeh = vfeh + temp
			
		if training == "light":
			pfeh = vfeh * 0.25
		elif training == "medium":
			pfeh = vfeh * 0.5
		elif training == "hard":
			pfeh = vfeh * 0.75
		elif training == "intense":
			pfeh = vfeh
			
		tfeh = pfeh + vfeh
		
		return tfeh
		

		
class Owner(object):
# A small object to hold the email-variable

	email = "None"

	def setEmail(self, email):
		self.email = email
		
	def getEmail(self):
		return self.email
		

		
class Stable(object):
# An object to hold the stalls-array
	stalls = []
	
	def printHorsesInStable(self):
		stable = None
		#with open('tempfile.txt', 'w') as tempFile
		#tempFile.write("These are your horses and what they need of feed for each day:")
		for horse in self.stalls:
			stable = "%s needs $s feH a day" % (horse.name, horse.feh)
			#tempFile.write(stable)
		return stable
