from sys import argv

script, input_file = argv

def print_all(f):
  print f.read()
# function print_all to print all content of input file

def rewind(f):
  f.seek(0)
# function rewind to go to beginning (0) of input file

def print_a_line(line_count, f):
  print line_count, f.readline()
# function print_a_line to print specific lines of input file

current_file = open(input_file)
# this is the variable to open input file

print "first let's print the whole file:\n"

print_all(current_file)
# print the whole input file

print "Now let's rewind, kinda like a tape.\n"

rewind(current_file)
# nothing happens at Terminal, just rewinding file

print "Let's print 3 lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
# print the 3 first lines of input file
