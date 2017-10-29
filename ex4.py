# Number of Cars
cars = 100

# Space for people in a car
space_in_a_car = 4.0

# Number of drivers
drivers = 30

# Number of passengers
passengers = 90

# Number of Cars not driven 
cars_not_driven = cars - drivers

# Number of cars driven
cars_driven = drivers

# Number of people that can carpool
carpool_capacity = cars_driven * space_in_a_car

# Average passengers per car
average_passengers_per_car = passengers / cars_driven


# Output the number of cars available
print("There are", cars, "cars available.")

# Output the number of drivers available
print("There are only", drivers, "drivers available.")

# Output the number of empty cars
print("There will be", cars_not_driven, "empty cars today.")

# Output the number of people that can travel
print("We can transport", carpool_capacity, "people today.")

# Output the number of people that want to travel
print("We have", passengers, "to carpool today.")

# Output the number of people in each car
print("We need to put about", average_passengers_per_car, "in each car.")