from user import User

class Privileges():                                      # Определение нового класса, который ничего не наследует
    def __init__(self, a):
        self.priv = a
        
    def show_priv(self):
        print(*self.priv, sep = ", ")
         
        
class Admin(User):
    """Класс-наследник"""
    def __init__(self, f_name, l_name, citizenship):
        super().__init__(f_name, l_name, citizenship)
        self.privileges = Privileges(['Granted to delete users', 'granted to ban users']) 

# Создание экземпляра класса Privileges и сохранение его в атрибуте класса-наследника Admin               
# Теперь при каждом вызове __init__() экземпляр класса Admin будет иметь автомат. созданный экземпляр Privileges