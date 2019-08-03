numbers = [1, 3, 5]
a = 2
b = 4
c = 6
more_numbers = [a, b, c]

print more_numbers

my_favorite_numbers = [22, 2, 8, 13]
for num in my_favorite_numbers:
    print 'I really like the number', num

my_grocery_list = []
# get items from the user, when he says STOP, print out the list
item = raw_input('Next item?')
while item != 'STOP':
# != is not equals (diferente de)
    my_grocery_list.append(item)

    item = raw_input('Next item?')

print(my_grocery_list)
