from horse import *

class Stable(object):

	stalls = []
	
	def printHorsesInStable(self):
		print "These are your horses:"
		for horse in self.stalls:
			print "%s is a %s %s" % (horse.name, horse.type, horse.gender)