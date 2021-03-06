# -*- coding: utf-8 -*- 

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) 

def print_first_word(words): #manglet ‘:’
    """Prints the first word after popping it off."""
    word = words.pop(0) #tatt bort en 'o'
    print word

def print_last_word(words): 
    """Prints the last word after popping it off."""
    word = words.pop(-1) #manglet ‘)’
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
where there is none. 
""" # fjernet 2x \t på siste linje


print "--------------"
print poem
print "--------------"

five = 10 - 3 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #endret ‘\’ til ‘/’
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point) #manglet en ‘)’, satte inn _ istedenfor - og korrigerte variabelnavnet


sentence = "All good things come to those who weight."

words = break_words(sentence) #tatt bort ex25. da funksjonen ligger i dette dokumentet
sorted_words = sort_words(words) #tatt bort ex25. da funksjonen ligger i dette dokumentet

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #fjernet ‘.’
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) #tatt bort ex25
print sorted_words #manglet ‘t’

print_first_and_last(sentence) #manglet en ‘f’ i funksjonsnavnet

print_first_and_last_sorted(sentence) #korrigerte variabel-navn, tok bort mellomrommene før funskjonsnavnet, korrigerte '_a_' til '_and_'
