# from sys import 
from program import * #bad idea to import everything?
#import horse			- virker ikke
#from stable import *	- virker ikke

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
		form = web.input(name="Nobody")
		name = "%s" % (form.name)
		return render.form(name=name)
	
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
	

