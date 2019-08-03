def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enuf for a party!"
    print "Get a blanket. \n"
# defined variable cheese_and_crackers made of cheese amd boxes_of_crackers
# we need to know how many of each we have for the party

print "we can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# amount of cheese and crackers we have

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# amount of cheese and crackers we have

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# amount of cheese and crackers we have

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# amount of cheese and crackers we have
