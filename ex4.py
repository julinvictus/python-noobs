cars = 100
# we have 100 cars at Fb
space_in_a_car = 4.0
# each car has 4 seats
drivers = 30
# only 30 ppl like traffic and are down to drive
passengers = 90
# 90 ppl work at Mpk
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
