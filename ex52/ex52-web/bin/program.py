# from sys import 
from program import * #bad idea to import everything?
#import horse			- virker ikke
#from program import owner	- virker ikke

import web

urls = (
	'/', 'Index'
)

program = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

class Index(object):
	
	def GET(self):
		return render.form()
	
	def POST(self):
		form = web.input(name="Nobody", horsename=None, type=None, gender=None)
		name = "%s" % (form.name)
		horsename = "%s" % (form.horsename)
		type = "%s" % (form.type)
		gender = "%s" % (form.gender)
		return render.index(name=name, horsename=horsename, type=type, gender=gender)
	
	def assignVariables(self):
		owner = Owner()
		stable = Stable()
		horse = Horse()
	
		owner.setName()

		horse.setAttributes()

		stable.printHorsesInStable()

		# horse.findEnergyNeed()

if __name__ == "__main__":
	program.run()
	

