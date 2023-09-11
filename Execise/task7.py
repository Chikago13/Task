
# 1. Реализовать класс Car с атрибутами название, километраж, страна производитель. Переопределять метод eq (на основании страны производителя), создать метод для обнуления километража.   
# Реализовать метод, возвращающий значение кол-ва созданных экземпляров.  
# 1.2. Создать функцию для генерирования заданного количества экземпляров.  
# 1.3. Создать функцию, которая будет сортировать полученный список по переданному параметру(атрибут экземпляру) 
from random import randint, sample
from operator import attrgetter

class Car:
    count = 0

    def __init__(self, name, kil, countru):
        self.name =name
        self.kil = kil
        self.countru = countru
        Car.count += 1
        Car.parametr = []

    def __eq__(self, other):
        return self.countru == other.countru
    
    def ziro_kil(self):
        self.kil = 0

    def car_count():
        return Car.count
    
    def __str__(self) -> str:
        return f'{self.name} {self.kil} {self.countru}'
    
    def __repr__(self) -> str:
        return f'{self.name} {self.kil} {self.countru}'
    
def gen_car(cont):
    ls = []
    car_mar = {'German':['Audi', 'BMV', 'Opel'], "Japan":['Toyta'], 'UKR':['Mini','Range'], 'Chine':['L9']}
    for _ in range(cont):
        countru = sample(car_mar.keys(), 1)[0]
        # countru = car_mar.keys()[randint(0, len(car_mar) -1)] 
        c_1 = Car(sample(car_mar[countru], 1), randint(0, 1000000), countru)
        ls.append(c_1)
    return ls

def sorted_list(list_val, parametr):
    list_val.sort(key=attrgetter(parametr))
    return list_val








res = gen_car(10)
# print(res)
# print(type(res))
print(sorted_list(res, 'countru'))

# c2 = Car('Audi', 1000, 'German')
# c3 = Car('BMW', 15000, 'Japan')

# print(c2)
# print(c3)
# print(c2 == c3)

    

        
    

    
    

