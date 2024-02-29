class Car():
    """"Модель автомобиля"""

    def __init__(self, manuf, model, year):
        """Инициализация атрибутов автомобиля"""
        self.manuf = manuf
        self.model = model
        self.year = year               
        self.odom_reading = 99 
    
    def description(self):
        """Отформатированное описание"""
        long_name = f"{self.manuf}, {self.model}, {self.year}"
        print("\n", long_name.title())

    def read_odom(self):
        """Отображает пробег машины"""
        print(f"The {self.manuf} has {self.odom_reading} km on it.")

    def update_odom(self, kilometrage):
        """Обновление пробега"""
        if kilometrage >= self.odom_reading:
            self.odom_reading = kilometrage
        else:
            print("You cant roll back an odometer.")

    def increm_odom(self, km):
        """Увеличивает показания с приращением"""
        self.odom_reading += km