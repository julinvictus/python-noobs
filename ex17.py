from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping from %s to %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "THE INPUT FILE IS %d BYTES LONG" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()
