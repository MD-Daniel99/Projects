from car import Car
    
class Battery():
    def __init__(self, battery_capacity = 75):
        """Инициализация атрибутов аккумулятора """
        self.capacity = battery_capacity

    def describe_battery(self):
        print(f"\nThe car has {self.capacity}-kWh battery.")

    def get_range(self):
        if self.capacity == 75:
            range = 260
        elif self.capacity == 100:
            range = 315
    
        print(f"\nThis car can go about {range} km on a full charge.")

    def upgrade_battery(self):
        if self.capacity < 100:
            self.capacity = 100

class ElectricCar(Car):
    """Аспекты машины, специфические для элеткричек"""
    def __init__(self, manuf, model, year):
        super().__init__(manuf, model, year)
        self.battery = Battery()