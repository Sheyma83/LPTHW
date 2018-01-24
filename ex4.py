#Number of cars
cars = 100
#Number of spaces in each car
space_in_a_car = 4.0
#Number of drivers
drivers = 30
#Number of passengers
passengers = 90
#Cars without drivers
cars_not_driven = cars - drivers
#Cars with drivers
cars_driven = drivers
#Cars * the space in car = the capacity
carpool_capacity = cars_driven * space_in_a_car
#All passengers /cars driven =  average number of passengers
average_passengers_per_car = passengers / cars_driven

print "there are" ,cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
