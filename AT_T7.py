print("Calculate fuel consumtion.")
Feed=int(input("Enter travel distance(kilometers): "))
Distance=Feed
Feed=int(input("Enter fuel usage(liters): "))
FuelUsage=Feed
Consumption=100/(Distance/FuelUsage)
Consumption=int(Consumption)
print(f"Fuel consumption is {Consumption} liter(s) per 100 km")