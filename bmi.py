#Ask the user for their BMI
bmi = float(raw_input('What is yr BMI? '))

# Determine if the user is
if bmi < 0:
    print "I don't believe you"
# 1. underweight
elif bmi < 18.5:
    print 'You are underweight'
elif bmi > 18.5 and bmi < 24.9:
# 2. normal underweight
    print "You're a normie"
elif 25 < bmi and bmi < 29.9:
# 3. overweight
    print "You're overweight"
else:
# 4. obese
    print "You are obese"
