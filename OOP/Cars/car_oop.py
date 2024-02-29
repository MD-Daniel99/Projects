import car
from electric_car import ElectricCar

#########################################
# Классы Car и ElectricCar импортируются

my_car = car.Car('Subaru', "Impreza WRX STI", 2014)   # Создание экземпляра класса
my_car.description()          

my_car.update_odom(101)
my_car.read_odom()    

my_car.increm_odom(10)
my_car.read_odom()   

my_electric = ElectricCar('tesla', 'model s', 2019)
my_electric.description()

my_electric.battery.describe_battery()
my_electric.battery.get_range()
my_electric.battery.upgrade_battery()
my_electric.battery.get_range()