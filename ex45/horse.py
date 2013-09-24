class Horse(object):

	name = "None"
	hight = "None"
	weight = "None"
	type = 	"None"
	gender = "None"

	def setAttributes(self):
		print "What is your horses name?"
		self.setName()
		
		print "What is your horses hight - in cm?"
		self.setHight()
		
		print "What is the type of your horse?"
		self.setType()
		
		print "What is the gender of your horse?"
		print "stallion, gelding or mare"
		self.setGender()
		
		print "Do you have any more horses?"
		print "yes or no"
		answer = raw_input(">")
		if answer == "yes":
			self.setAttributes()
		
	def setName(self):
		self.name = raw_input('>')
		
	def setHight(self):
		self.hight = raw_input('>')
		
	def setType(self):
		self.type = raw_input('>')
		
	def setGender(self):
		self.gender = raw_input('>')