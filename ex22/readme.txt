Siden vi har gjort mye programmeringer er det ikke alt som er like vanskelig å klare å huske. Noe syntax 
er greit for meg å huske. Derfor har jeg kun skrevet ned det jeg tror jeg på et eller annet tidspunkt vil 
ha behov for å slå opp igjen. Enten ganske tidlig, eller om noen uker til. Dette kan da også være 
greit å ha skrevet ned en plass slik at jeg lett for å finne det igjen hvis jeg kommer borti noen av 
disse elementene, eller ikke klare å huske hvordan en spesiell syntax er. 

Python - viktige elementer

print “for å printe tekst til sida”
# for å kommentere
variabelnavn = ‘for å deklarere en variabel’.
print “Bruk %r/s eller d for å bruke gitt en gitt variabel inne i setninga” % variabelnavn

# -- coding: utf-8 -- hvis man bruker ikke-ASCII tegn

%s, %r, and %d er 'formatters'
Bruk %r for debugging (siden den viser 'rådata' av variabelen. De andre er brukt for visning til brukere)

Funksjoner: angis med
def funskjonsnavn(parametere):
	hva funksjonen skal gjøre

Brukes ved
funksjonsnavn(parametere)

*args brukes i spesielle tilfeller hvor python tar alle parametrene og legger de i ei liste.