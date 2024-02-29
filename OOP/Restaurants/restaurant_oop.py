from restaurant import Restaurant, Bufeit


rest = Restaurant('Whoah Zieng Chiao Ma','Armeninan')
cafe = Restaurant('Nezjniy Sybyriak', 'Slavic')
buffee = Bufeit('Kulturnaya Stolitsa', 'Rus')               # Создание экземпляра класса буфет. Строка также приказывает вызвать класс-родитель Restaurant
# Restaurant
print(f"\n\t!!?{rest.name}, {rest.type}!?!")
rest.describe()
rest.open()
rest.num_served(21)                                         # Изменение значения атрибута по умолчанию путем передачи аргумента
rest.increment(8)                                           # Изменение значения атрибута по умолчанию путем приращения
# Cafe
print(f"\n\t!!?{cafe.name}, {cafe.type}!?!")
cafe.describe()
cafe.open()
print(cafe.type)

# Buffee                                                    # Вызов 
buffee.theatre_list()

