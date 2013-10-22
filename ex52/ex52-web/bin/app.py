# from sys import
from modules import Horse
from modules import Stable
from modules import Owner


import web

urls = (
	'/', 'Index'
)

program = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

class Index(object):
	
	owner = Owner()
	stable = Stable()
	horse = Horse()
	
	def GET(self):
		return render.form()
	
	def POST(self):
		form = web.input(horsename=None, type=None, gender=None, morehorses=None, email=None, training=None, hight=None)
		self.setHorseVariables(form.horsename, form.type, form.gender, form.training, form.hight)
		
		horsename = self.horse.getName()
		type = self.horse.getType()
		gender = self.horse.getGender()
		feh=self.horse.getFeh()
				
		self.owner.setEmail(form.email)
		email = self.owner.getEmail()
		
		morehorses = "%s" % (form.morehorses)
		if morehorses == "yes":
			return render.form()
		else:
			horses=self.stable.stalls
			return render.index(morehorses=morehorses, horsename=horsename, type=type, gender=gender, email = email, feh=feh, horses=horses)

	
	def blankForm(self):
		return render.form()
	
	def setHorseVariables(self, horsename, type, gender, training, hight):
		self.horse.setName(horsename)
		self.horse.setType(type)
		self.horse.setGender(gender)
		self.horse.setTraining(training)
		self.horse.setHight(hight)
		self.horse.findEnergyNeed()
		self.horse.putHorseInStable(self.stable) #saves entered horse in stable
		
		self.horse = Horse()

if __name__ == "__main__":
	program.run()