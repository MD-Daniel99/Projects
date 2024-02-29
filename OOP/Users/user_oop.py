import user as u
from priv_admin import Admin

user1 = u.User('Smitty', 'Bigass', 'Texas')                
user2 = u.User('Jorj','Rimsky', 'Sweden')
user3 = u.User('Nezjniy', 'Slavic', 'Rus')
administrator = Admin("Naftula" , "Nurenbertchik", "Israel") # Создание экземпляра класса Admin. Строка также приказывает вызвать класс-родитель User

user1.describe()
user2.describe()
user3.describe()

user1.log_attempts(3)                           # Изменение значения атрибута по умолчанию путем передачи аргумента
user1.reset_att()                  

administrator.greet()
administrator.privileges.show_priv()    # Приказ обратиться к экземпляру administrator, найти его атрибут privileges и вызвать метод show_priv, связанный с 
                                        # экземпляром Privileges из атрибута