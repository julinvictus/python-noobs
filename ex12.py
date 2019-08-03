age = raw_input ("How old are you? ")
height = raw_input ("How tall are you? ")
weight = raw_input ("How much do you weight? ")
fb = raw_input ("How long have you worked for Fb? ")

print "So you're %r old, %r tall, %r heavy and have worked for Fb for %r." % (
    age, height,  weight, fb)

print "So you're %r old,\n %r tall,\n %r heavy\n and have worked for Fb for %r." % (
        age, height,  weight, fb)
# I added \n to skip lines here
