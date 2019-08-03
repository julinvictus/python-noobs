from sys import argv

# python bonus3_2.py input.txt cat dog
script, filename, findword, replaceword = argv

# open input filename
readfile = open(filename)

# print "This is your file %r:\n" % filename
# print readfile.read()
# It got too complicated, skipped print for now

# read the contents
contents = readfile.read()

# replace cat with dog
contents = contents.replace(findword, replaceword)

print "\nREPLACING STUFF NOW...Use CAT command to see the file!\n"

# output to <filename>.new
writefile = open(filename + '.new', "w")
writefile.write(contents)

readfile.close()
writefile.close()

# print "This is your new file %r:" % writefile
# print writefile.read()
# It got too complicated, skipped print for now
