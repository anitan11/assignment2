# from sys import
from modules import Horse
from modules import Owner


import web

urls = (
	'/', 'Form'
)

program = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

owner = Owner()
stalls = []

class Form(object):
	
	def GET(self):
	# This function renders the form whenever a GET-request is requested from /
	# But first it deletes all the objects previously stored in the list, stalls.
		del stalls[:]
		return render.form(horsename="No name", type="No type", gender="No gender", feh=0, horses=stalls)
	
	def POST(self):
	# A horse object is created in this POST-function for the application to be able to distiguish the horse-objects from each other.
	# A list is created, stalls, to hold the various horses.
	# This function then creates a variable, form, that holds the input from the form in form.html. These input-elements are then used in the 
	# setHorseVariables-function. Then som local variables are set with some get-functions in the Horse-class. The owners e-mail 
	# (thought about using the owners name at first, but an e-mail seemed a bit more logic to use) is stored in the an owner-object.
	# In the end, this function checks if the owner has more horses. If the owner chose yes in the form, the form will be rendered over
	# again, and some information about the previous entered horse, will be sent to form.html. If the owner chose no in the form, the index.html 
	# (yes, I know it is wrong to call it index.html at this point) will be rendered, and the information about the horses will be shown on the site.
	
		horse = Horse()
		horses=stalls
		
		form = web.input(horsename=None, type=None, gender=None, morehorses=None, email=owner.email, training=None, hight=None, weight=None)
		self.setHorseVariables(form.horsename, form.type, form.gender, form.training, form.hight, horse, form.weight)
		
		horsename = horse.getName()
		type = horse.getType()
		gender = horse.getGender()
		feh=horse.getFeh()
				
		owner.setEmail(form.email)
		email = owner.getEmail()

		morehorses = "%s" % (form.morehorses)
		if morehorses == "yes":
			return render.form(horsename=horsename, type=type, gender=gender, feh=feh, horses=horses)
		else:
			return render.index(horsename=horsename, type=type, gender=gender, email = email, feh=feh, horses=horses)
	
	def setHorseVariables(self, horsename, type, gender, training, hight, horse, weight):
	# This function is responsible for setting variables in the horse object, and also put the horse object in the stalls-list.
		horse.setName(horsename)
		horse.setType(type)
		horse.setGender(gender)
		horse.setTraining(training)
		horse.setHight(hight)
		horse.setWeight(weight)
		horse.findEnergyNeed()	#calculates the energy need for the horse
		stalls.append(horse) #saves entered horse in stable

if __name__ == "__main__": #This one makes it all run... I think...
	program.run()