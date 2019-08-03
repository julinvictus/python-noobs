print "WELCOME TO THE CARNIVAL!\n"
print "Not sure where to go?\n"
print "We can help ya!\n"


print "1. Rollercoaster\n"
print "2. Ferris Wheel\n"
print "3. Carousel\n"
print "4. Bumper cars\n"

answer = float(raw_input('Pick one thing, type its number: '))

if answer == 1:
    print "Do you like speed? y or n"
    speed = raw_input("> ")
    if "y" in speed:
        print "You gonna love it!"
    elif "n" in speed:
        print "You gonna puck.."

elif answer == 2:
    print "Are you afraid of heights? y or n"
    heights = raw_input("> ")
    if "y" in heights:
        print "You gonna be scared to death.."
    elif "n" in heights:
        print "You gonna love it!"

elif answer == 3:
    print "Are you a child? y or n"
    child = raw_input("> ")
    if "y" in child:
        print "You gonna love it!"
    elif "n" in child:
        print "It's boring.."

elif answer == 4:
    print "Do you like driving? y or n"
    driving = raw_input("> ")
    if "y" in driving:
        print "You gonna love it!"
    elif "n" in driving:
        print " You gonna feel like hell.."

else:
    print "Sorry we just have 4 attractions."
