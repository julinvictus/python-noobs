

print "What's yr first name?"

first_name = raw_input ()

print "What's yr last name?"

last_name = raw_input ()

counting_letters = len(first_name+last_name)

print "Yr name (%s %s) has %r letters" % (first_name.upper(), last_name.upper(), counting_letters)
