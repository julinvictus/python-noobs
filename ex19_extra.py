# romeu e julieta is a Brazilian candy made of
# cheese and goiabada (guava paste)

def romeu_e_julieta (cheese_count, boxes_of_goiabada):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of goiabada!" % boxes_of_goiabada
    print "Man that's enuf for a Brazilian party!"
    print "Get a cachassa. \n"

print "We can just give the function numbers directly:"
romeu_e_julieta (20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_goiabada = 50

romeu_e_julieta (amount_of_cheese, amount_of_goiabada)

print "We can even do math inside too:"
romeu_e_julieta (10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
romeu_e_julieta (amount_of_cheese + 100, amount_of_goiabada + 1000)
