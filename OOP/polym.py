# from rect_sq import Rectangle, Square

# rect_1 = Rectangle(3,4)
# rect_2 = Rectangle(12,5)

# square_1 = Square(5)
# square_2 = Square(10)

# figures = [rect_1, rect_2, square_1, square_2]

# for fig in figures:
#     if isinstance(fig, Square):
#         print(f"Square: {fig.get_area()}")
#     else:
#         print(f"Rectangle: {fig.get_area()}")
    
class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    # добавим новое поле - шкала счастья
    @property
    def happiness(self):
        return self._happiness

    # с помощью декоратора setter мы можем неявно передать во второй 
    # аргумент значение, находящееся справа от равно, а не закидывать это 
    # значение в скобки, как мы это делали в модуле C1, когда не знали о 
    # декораторах класса 
    @happiness.setter
    # допустим, мы хотим, чтобы счастье питомца измерялось шкалой от 0 до 100
    def happiness(self, value):
        if value <= 100 and value >= 0:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
jane.happiness = 100  # осчастливим нашу собаку < :
print(jane.human_age)
print(jane.happiness)