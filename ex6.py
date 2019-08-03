x = "There are %d types of people." % 10
# one variable
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# 2 variables, gotta use parenthesis

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y
# both variables show between single-quotes

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
# print both variables side by side

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# print both variables side by side
