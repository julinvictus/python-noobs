numbers = {'1': 'one', '2': 'two',
    '3': 'three', '4': 'four', '5': 'five',
    '6': 'six', '7': 'seven', '8': 'eight',
    '9': 'nine', '0': 'zero'}

def find_phone(thenum, numbers):
    if numbers in thenum:
        return thenum[numbers]
    else:
        return "Not found."

numbers['_find'] = find_phone


while True:
    print "What's yr phone number? ",
    phone_number = raw_input("> ")

    if not phone_number: break

    spell = numbers['_find'](numbers, phone_number)
    print spell

# only printing one number :(
