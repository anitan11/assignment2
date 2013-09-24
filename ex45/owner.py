class Owner(object):

	# def __init__(self)

	name = "None"
	noHorses = 0

	def setName(self):
		self.name = raw_input('>')
		self.noHorses = self.noHorses + 1
		