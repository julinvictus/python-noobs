from sys import argv

script, filename = argv

txt = open(filename)

print "Here's yr file %r:" % filename
# this shows you the name of the txt file you typed at terminal
print txt.read()
# this shows the txt file content

print "I'll also ask you to type it again:"
file_again = raw_input("> ")
# just type again the name of the file

txt_again = open(file_again)

print txt_again.read()
