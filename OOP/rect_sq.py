
class Square:
    def __init__(self, a):
        self.a = a   
	
    def get_area(self):		
        return self.a ** 2
    

class Rectangle(Square):
    def __init__(self,a, b):
        super().__init__(a)
        self.b = b

    def get_area(self):		
        return self.a * self.b