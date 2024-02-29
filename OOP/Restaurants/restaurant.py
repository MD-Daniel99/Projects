class Restaurant():
    def __init__(self, r_name, c_type):
        self.name = r_name
        self.type = c_type
        self.served = 0                 # Атрибут по умолчанию

    def describe(self):
       print(f"\nName: {self.name}, type: {self.type}")
    
    def open(self):
        print(f"{self.name} is opened!\n")

    def num_served(self, costumers_served):
        self.served = costumers_served

    def increment(self, increm):
        self.served += increm
        print(f"\n{self.served} costumers are served in total.")

class Bufeit(Restaurant):                                   # Класс - потомок
    def __init__(self, r_name, c_type):                     # Наследование атрибутов класса - родителя
        super().__init__(r_name, c_type)
        self.theatre = ['Na Strastnom', 'Bolshoy', 'Malyi']

    def theatre_list(self):
        print(*self.theatre, sep = ", ")
