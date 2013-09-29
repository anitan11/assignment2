# from sys import *
from owner import *
from horse import *
from stable import *

import web

urls = ( '/', 'Index' )

program = web.application(urls, globals())
render = web.template.render('templates/')

class Index(object):
	
	owner = Owner()
	stable = Stable()
	horse = Horse()
	
	owner.setName()

	horse.setAttributes()

	stable.printHorsesInStable()

	# horse.findEnergyNeed()

