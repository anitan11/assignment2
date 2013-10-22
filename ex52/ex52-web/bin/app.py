# from sys import
from modules import Horse
from modules import Stable
from modules import Owner


import web

urls = (
	'/', 'Form'
)

program = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

owner = Owner()
stable = Stable()
stalls = []

class Form(object):
	
	def GET(self):
		del stalls[:]
		return render.form(horsename="No name", type="No type", gender="No gender", feh=0, horses=stalls)
	
	def POST(self):
		horse = Horse()
		form = web.input(horsename=None, type=None, gender=None, morehorses=None, email=owner.email, training=None, hight=None)
		self.setHorseVariables(form.horsename, form.type, form.gender, form.training, form.hight, horse)
		
		horsename = horse.getName()
		type = horse.getType()
		gender = horse.getGender()
		feh=horse.getFeh()
				
		owner.setEmail(form.email)
		email = owner.getEmail()
		
		morehorses = "%s" % (form.morehorses)
		
		horses=stalls
		if morehorses == "yes":
			return render.form(horsename=horsename, type=type, gender=gender, feh=feh, horses=horses)
		else:
			return render.index(horsename=horsename, type=type, gender=gender, email = email, feh=feh, horses=horses)
	
	def setHorseVariables(self, horsename, type, gender, training, hight, horse):
		horse.setName(horsename)
		horse.setType(type)
		horse.setGender(gender)
		horse.setTraining(training)
		horse.setHight(hight)
		horse.findEnergyNeed()
		stalls.append(horse) #saves entered horse in stable

if __name__ == "__main__":
	program.run()