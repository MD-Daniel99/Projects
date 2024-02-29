class User():
    """Параметры пользователей"""
    def __init__(self, f_name, l_name, citizenship):
        self.name = f_name
        self.surname = l_name
        self.cit = citizenship
        self.login_att = 0
    
    def describe(self):
        print(f"\nUser: {self.name} {self.surname}, {self.cit}")
        self.greet()                                       # Ссылка на текущий объект(экземпляр класса) - способ вызова метода внутри другого
    
    def greet(self):
        print(f"Hey, {self.name} {self.surname}, son of the {self.cit}")
    
    def log_attempts(self, attempts):
        self.login_att += attempts
        print(self.login_att)
    
    def reset_att(self):
        self.login_att = 0
        print(self.login_att)
