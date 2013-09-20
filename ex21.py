# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# BY HAND
# iq 			= divide(100, 2) 	= 50
	# what = add(age, subtract(height, multiply(weight, divide(50, 2))))
	
# divide(50, 2)	= (50 / 2) 			= 25
	# what = add(age, subtract(height, multiply(weight, 25)))
	
# weight 		= multiply(90,2) 	= 180
	# what = add(age, subtract(height, multiply(180, 25)))
	
# multiply(180, 25) 	= 4500
	# what = add(age, subtract(height, 4500))
	
# height = subtract(78, 4) = 74
	# what = add(age, subtract(74, 4500))

# subtract(74, 4500) 		= -4426
	# what = add(age, -4426)
	
#age = add(30, 5) = 35
	# what = add(35, -4426)

# what = -4391

#sjekket restultatet etterpå, og det er korrekt

print "That becomes: ", what, "Can you do it by hand?"

