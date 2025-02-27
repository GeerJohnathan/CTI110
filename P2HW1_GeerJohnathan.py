#GeerJohnathan
#27FEB2024
#P2HW1
#Reformatting a pre existing code

print("This program calculates and displays travel expenses")
print()
base_budget = float(input('Enter Budget: '))
travel_destination = input('Enter your travel destination: ')
fuel_cost = float(input('How much do you think you will spend on gas? '))
hotel_cost = float(input('Approximately, how much will you need for accomodation/hotel? '))
food_cost = float(input('Last, how much do you need for food? '))
print()
print('----------Travel Expenses----------')
print(f'Location:          {travel_destination}')
print(f'Initial Budget:    ${base_budget:.2f}')
print(f'Fuel:              ${fuel_cost:.2f}')
print(f'Accomodation:      ${hotel_cost:.2f}')
print(f'Food:              ${food_cost:.2f}')
print('-----------------------------------')
print(f'Remaining Balance: ${base_budget - fuel_cost - hotel_cost - food_cost:.2f}')

