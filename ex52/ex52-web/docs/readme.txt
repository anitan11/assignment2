Author: Anita Ruud Nilsen
Contact: anitarn5@gmail.com

Hvordan kjøre denne applikasjonen:
- Installer Python 2.3 <et-eller annet>
- Installer en webserver, f.eks. lpthw
- Kjør 'python bin/app.py' i cmd/terminal
- Applikasjonen skal nå være tilgjengelig på 'localhost:<angitt port til webserver>'

Tester:
- Installer Python 2.7.5 <et-eller annet>
- Kjør 'pyhton' i cmd/terminal
- Kjør ønsket test

Refleksjoner:
Assignment 2 - IS-206

Jeg spurte Janis om jeg ble nødt til å lage et spill, da forklaringen i oppgaveteksten til assignmentet og
på learningpythonthehardway var forskjellig. Jeg fikk svar at vi stod nokså fritt til å velge hva slags
'intelligent agent' vi ønsket å lage. Jeg ville da lage en applikasjon som regner ut hvor mye energi en
hest trenger pr dag, basert på noe som kalles 'normfôring av hest'. Jeg lagde applikasjonen istedenfor 
spillet fordi jeg ønsket å lage noe som ikke var likt det andre hadde laget, og jeg følte jeg ville få bedre
mulighet til å inkludere forskjellige typer segmenter av kode. 

Teorien bak denne applikasjonen er noe jeg har lært da jeg gikk på en landbruksskole for noen år siden, og
teorien ble presentert verbalt i timer. Derfor har jeg ingen referanser å vise til.

Det siste problemet jeg hadde var at kalkuleringene ble feil. Jeg fant ut av hva jeg hadde gjort galt. Jeg 
kom plutselig på at hestens vekt ikke kan bli kalkulert ut fra høyden. Man trenger å ta et mål rundt 
brystet på hesten, et såkalt 'brystomfang', der hvor gjorta skal ligge. Deretter tar man 

'brystomfang * 6,25 - 625'

Jeg fikset dette ved å legge til et nytt felt i skjemaet, og brukeren må selv finne ut av hestens vekt.

Jeg tror jeg kunne ha gjort ganske mye mer med denne applikasjonen, som å legge til mer css (dette er 
ikke et css-kurs), idiotsikre applikasjonen etc etc. Men jeg syntes at jeg ble nødt til å begrense 
hvor mye jeg ønsket å gjøre siden vi har andre assignments som også skal gjøres.

'Your final exam'-punktene:
Jeg hadde litt problemer med å få noen av punktene til å relatere direkte til min applikasjon, men punkt 4
fikk jeg relatert slik:
Skjema til å skrive inn informasjon om hesten = login + hestene som er lagt inn blir skrevet ut som en 
liste senere, hvor det kommer opp informasjon om hesten = highscoreliste.



One thing I didn't figure out is how to import classes from another folder. That is why there is a
modules.py-file in both the bin-direcorty and the program-directory.

Skriv om:
- har ikke fokusert så mye på css da dette ikke er et css-kurs (Applikasjonen er oversiktlig uten css)

Guider:
- hvordan kjøre applikasjonen
- hvordan kjøre testene