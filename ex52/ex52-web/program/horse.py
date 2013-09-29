from stable import *

class Horse(object):

	name = "None"
	hight = "None"
	weight = "None"
	type = 	"None"
	gender = "None"
	vfeh = "None"
	pfeh = "None"
	tfeh = "None"

	def setAttributes(self):
		self.setName()
		
		self.setHight()
		
		self.setType()
		
		self.setGender()
		
		self.putHorseInStable()
		
		answer = raw_input(">")
		if answer == "yes":
			horse = Horse()
			horse.setAttributes()
		
	def setName(self):
		self.name = raw_input('>')
		
	def setHight(self):
		self.hight = raw_input('>')
		
	def setType(self):
		self.type = raw_input('>')
		
	def setGender(self):
		self.gender = raw_input('>')
		
	def putHorseInStable(self):
		self.stable = Stable()
		self.stable.stalls.append(self)
		
	def findEnergyNeed(self):
		self.weight = self.hight * 6,25 - 625
		
		if self.hight > 148:
			self.vfeh = self.weight / 100
		elif self.hight < 148:
			self.temp = self.weight / 100
			self.vfeh = temp * 0,8
			
		if type == "varmblodshest":
			temp = vfeh * 0,05
			vfeh = vfeh + temp
		elif type == "kaldblodstraver":
			temp = vfeh * 0,05
			vfeh = vfeh + temp
		elif type == "fullblodshest":
			temp = vfeh * 0,10
			vfeh = vfeh + temp
		
		if gender == "stallion":
			temp = vfeh * 0,10
			vfeh = vfeh + temp
			
		if trening == "light":
			pfeh = vfeh * 0,25
		elif trening == "medium":
			pfeh = vfeh * 0,5
		elif trening == "hard":
			pfeh = vfeh * 0,75
		elif trening == "intense":
			pfeh = vfeh
			
		tfeh = pfeh + vfeh
		
		print "%s needs %f feH pr day" % (name, tfeh)