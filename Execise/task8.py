from random import randint, choice


class House:
    price: int
    square: int

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
    name: str
    surname:str
    account: int

    def __init__(self, name, surname, account):
        self.name = name
        self.surname = surname
        self.account = account

    def __str__(self) -> str:
        return f'name: {self.name} surname: {self.surname} account: {self.account}'
    
    def __repr__(self) -> str:
        return f'name: {self.name} surname: {self.surname} account: {self.account}'
    

        
    
def gen_house_list(count: int):
    result = []
    for _ in range(count):
        result.append(House(price=randint(10000, 1000000), square=randint(50, 200)))
    return result




NAMES = ["Adams", "Baker", "Clark", "Davis", "Evans", "Frank", "Ghosh"]
SURNAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]

def gen_consumer():
    random_consumer = Consumer(name=choice(NAMES), surname=choice(SURNAMES), account=randint(10000, 1000000))
    return random_consumer



def get_recommendation(consumer, house_list):
    print(consumer, house_list)
    filter_list = list(filter(lambda x: x.price <=consumer.account, house_list))
    result = sorted(filter_list, key=lambda x: x.square, reverse = True)
    return result



# h = House()
# c = Consumer()

# print(gen_house_list(10))
# print(gen_consumer())
print(get_recommendation(gen_consumer() ,gen_house_list(10)))

