# script to decide: take car or bus?

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
# more cars than ppl
elif cars < people:
    print "We should not take the cars."
# less cars than ppl, not enough
else:
    print "We can't decide."
# same amount of both, whatever

if buses > cars:
    print "That's too many buses."
# more buses than cars
elif buses < cars:
    print "Maybe we could take the buses."
# less buses than cars
else:
    print "We still can't decide."
# same amount of buses and cars

if people > buses:
    print "Alright, let's just take the buses."
# more ppl than buses
else:
    print "Fine, let's stay home then."
# less ppl than buses, or same amount
