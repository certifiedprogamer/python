import utilities
import car

print(utilities.get_lowest_num(2, 4, 6, 9, 10))

my_car = car.Car("Chevy", "Silverado", 21)
my_car.go()


my_other_car = car.Car("Ford", "F150", 25)
my_other_car.go()

# cheapest car to take 400 miles
car1_cost = my_car.calculate_trip_cost(400, 3.58)
car2_cost = my_other_car.calculate_trip_cost(400, 3.78)

print(f"{my_car.make}: {car1_cost}")
print(f"{my_other_car.make}: {car2_cost}")
