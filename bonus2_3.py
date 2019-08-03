# asks the user for their five favorite movies then shows them the list

print "What is yr fav movie?"

movie1 = raw_input ("> ")

print "What is yr 2nd fav movie?"

movie2 = raw_input ("> ")

print "What is yr 3rd fav movie?"

movie3 = raw_input ("> ")

print "What is yr 4th fav movie?"

movie4 = raw_input ("> ")

print "What is yr 5th fav movie?"

movie5 = raw_input ("> ")

print """
So yr movie rankings are:
1. %s
2. %s
3. %s
4. %s
5. %s
""" % (movie1, movie2, movie3, movie4, movie5)
