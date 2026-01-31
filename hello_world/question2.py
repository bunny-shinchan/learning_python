#Write a program that takes user weight in pounds and convert it into KG

weight_in_pounds = input('Type your weight in pounds.')
print(type(weight_in_pounds))


weight_in_kg = 0.453592 * float(weight_in_pounds)

print(type(weight_in_kg))

print('Your weight in kg is then ' + str(weight_in_kg))
