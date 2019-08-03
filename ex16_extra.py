# Watch out for capital letters on statements like print
# cause then code won't work :(

from sys import argv

script, filename = argv

txt = open(filename)

print "This is the file we're opening now: %r " % filename

print txt.read()
