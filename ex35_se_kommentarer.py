from sys import exit	#importerer exit-funksjonen fra sys

def gold_room():
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")	#bruker velges hvor mye gull som han/hun skal ta
    if "0" in next or "1" in next:
        how_much = int(next)  # raw_input konverteres fra string til tall
    else:	# hvis bruker ikke tastet et tall, så kalles dead-funksjonen med gitt tekst
        dead("Man, learn to type a number.")

    if how_much < 50:		#bruker må taste et tall under 50, ellers kalles dead-funksjonen med gitt tekst
        print "Nice, you're not greedy, you win!"
        exit(0)		# spillet avsluttes
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ") #bruker må velge en handling

        if next == "take honey": # Hvis bruker tar honning, så kalles dead-funksjonen med gitt tekst som parameter
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved: # hvis bruker terger bjørnen, så printes det ut melding, og bear_moved-variabelen settes til true
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:	# hvis bjørnen terges igjen, så kalles dead-funksjonen med gitt tekst
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved: # hvis bruker velger å åpne dør, så kalles gold_room-funksjonen
            gold_room()
        else:		#  hvis ikke tekst er gjenkjennbar, så skrives følgende tekst ut til brukeren
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ") #Bruker må velge å flykte eller å spise hodet sitt(?)

    if "flee" in next:	# hvis bruker flykter, så begynner spillet på nytt med start-funksjonen
        start()
    elif "head" in next:	#hvis bruker velger å spise hodet sitt, så kalles dead-funksjonen med gitt tekst
        dead("Well that was tasty!")
    else:
        cthulhu_room()	#hvis ingen av delene velges, så kalles denne funksjonen på nytt


def dead(why):
    print why, "Good job!"	#skriver ut hva som er angitt i variabelen why
    exit(0)			#avslutter spillet

def start():   
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")  # user input som forteller hva brukeren vil gjøre, ta døre til høyre eller venstre

    if next == "left":	# hvis døra til venstre velges, så kalles funksjonen bear_room
        bear_room()
    elif next == "right":	# hvis døra til høyre velges, så kalles funksjonen cthulhu_room
        cthulhu_room()
    else:	# hvis ingenting velges, så kalles funksjonen dead med gitt tekst
        dead("You stumble around the room until you starve.")


start()  #starter funksjonen start