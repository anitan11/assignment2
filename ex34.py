print "What number in the list do you want to show?"
number = raw_input('>')
number = int(number, base=5)
number = number - 1

animals = ['bear', 'tiger', 'penguin', 'zebra']
bear = animals[number]

print bear