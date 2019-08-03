filename = raw_input('Filename?')
f = open(filename)
line_num = 1

print line_num, f.readline()

line_num += 1
print line_num, f.readline()

line_num += 1
print line_num, f.readline()
