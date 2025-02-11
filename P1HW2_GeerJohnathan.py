#GeerJohnathan
#11FEB2024
#P1HW1
#Creating a program that does basic math for calculating vacation expenses

#Need to: Ask user what their budget is, How much they will spend on Fuel, Hotel, and Food, then need to calculate what their remaining balance is after: Budget-Fuel-Hotel-Food

print("This program calculates and displays travel expenses")
print()
base_budget = int(input('Enter Budget:'))
travel_destination = input('Enter your travel destination:')
fuel_cost = int(input('How much do you think you will spend on gas?'))
hotel_cost = int(input('Approximately, how much will you need for accomodation/hotel?'))
food_cost = int(input('Last, how much do you need for food?'))
print()
print('----------Travel Expenses----------')
print('Location', travel_destination)
print('Initial Budget:', base_budget)
print()
print('Fuel:', fuel_cost)
print('Accomodation:', hotel_cost)
print('Food:', food_cost)
print()
print('Remaining Balance:', base_budget - fuel_cost - hotel_cost - food_cost)
