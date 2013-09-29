# from sys import 
from program import * #bad idea to import everything?
import horse
from stable import *

import web

urls = (
	'/', 'Index'
)

program = web.application(urls, globals())
render = web.template.render('templates/')

class Index(object):
	
	def GET(self):
		return render.index()
	
	def POST(self):
		form = web.input(name="Nobody")
		name = "%s" % (form.name)
		return render.index(name = name)
		
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
	

