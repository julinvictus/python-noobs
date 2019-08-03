filename = raw_input('Filename?')
f = open(filename)
line_num = 1

# use a loop and keep printing out
# [line number][line]
# line = f.readline()
# while we_arent_at_the_last_line:
#    print line_num, line
#    line_num += 1
#    line = f.readline()

for line in f.readlines():
#    line = line.stip('\n')
# if you wannna remove line
    print line_num, line,
    line_num += 1

# test it
