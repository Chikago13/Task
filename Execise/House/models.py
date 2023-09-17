__all__ = {'House', 'Consumer'}

class House:

    def __init__(self, price, square):
        self.price = price
        self.square = square
    
    def make_discount(self):
        pass
    
    def __str__(self) -> str:
        return f' price:{self.price} square:{self.square}'
    
    def __repr__(self) -> str:
        return f' price:{self.price} square:{self.square}'

class Consumer:

    def __init__(self, name, surname, account):
        self.name = name
        self.surname = surname
        self.account = account

    def __str__(self) -> str:
        return f'name: {self.name} surname: {self.surname} account: {self.account}'
    
    def __repr__(self) -> str:
        return f'name: {self.name} surname: {self.surname} account: {self.account}'