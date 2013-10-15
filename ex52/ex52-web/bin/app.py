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
		form = web.input(horsename=None, type=None, gender=None, morehorses="no", email=None, training=None)
		self.horse.setName(form.horsename)
		horsename = self.horse.getName()
		self.horse.setType(form.type)
		type = self.horse.getType()
		self.horse.setGender(form.gender)
		gender = self.horse.getGender()
		self.horse.setTraining(form.training)
		
		self.owner.setEmail(form.email)
		email = self.owner.getEmail()
		
		morehorses = "%s" % (form.morehorses)
		if morehorses == "yes":
			#to do: save entered horse in stable
			render.form()
		else:
			feh=self.horse.findEnergyNeed()
			return render.index(morehorses=morehorses, horsename=horsename, type=type, gender=gender, email = email, feh=feh)
	
	def assignVariables(self):
		stable.printHorsesInStable()

		# horse.findEnergyNeed()

if __name__ == "__main__":
	program.run()