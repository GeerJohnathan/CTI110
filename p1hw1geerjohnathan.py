#GeerJohnathan
#06FEB2024
#P1HW1
#Using python to code math without hard set integers

print("------Calculating Exponenets-----")
base_value = int(input('Enter an integer as the base value:'))
exponent_value = int(input('Enter an integer as the exponent:'))
powered_value = base_value ** exponent_value
print()
print('-' * 30)
print()
print(base_value, "raised to the power of", exponent_value, "is", powered_value, "!!")
print()
print()
print("------Addition and Subtraction-----")
starting_integer = int(input('Enter a starting integer:'))
addition_integer = int(input('Enter an integer to add:'))
subtraction_integer = int(input('Enter an integer to subtract:'))

solved_integer = starting_integer + addition_integer - subtraction_integer
print()
print('-' * 30)
print()
print(starting_integer,"+",addition_integer,"-",subtraction_integer,"is equal to", solved_integer)