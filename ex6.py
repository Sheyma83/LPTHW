# - - coding: utf- 8 - -
x = "There are %d types of people." %50
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
print "I said : %r." % x
print " Also I said : %s." % y 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious


a = "This is the left side of..."
b = "a string with a right side."

print a + b 
