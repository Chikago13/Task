# Создайте класс "Транспортное средство", у которого будут атрибуты "скорость", "вместимость" и методы "едь" и "остановись". 
# От этого класса унаследуйте классы "Автобус" и "Поезд", которые будут иметь свои специфические методы и атрибуты, например, метод "открыть двери" и атрибут "номер маршрута" 
# у класса "Автобус". Метод "прицепить вагон" и атрибут "вагон-ресторан" у класса "Поезд".
# В каждом классе реализуйте счетчик экземпляров. Используйте декоратор @classmethod. Создайте функцию, генерирующую заданное кол-во экземпляров класса поезд/автобус и 
# возвращающую список этих экземпляров. Создайте функцию, которая выполнит сортировку экземпляров по переданному параметру "скорость", "вместимость". 
from random import randint, choice

COMMANDS_NAMES = ['A1', 'A2', 'B1', 'B2', 'B3', 'G1', 'G2', 'G3', 'T1', 'T2', 'T3', 'R1', 'R2', 'R3']


class Transport:
    count = 0


    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity
        Transport.count +=1


    def go(self):
        return f'go'
    
    def stop(self):
        return f'stoped'
    

    @classmethod
    def generate_instances(cls, num):
        instances = []
        for _ in range(num):
            speed = randint(20, 100)
            capacity = randint(1, 250)
            instance = cls(speed, capacity)
            instances.append(instance)
        return instances
    
    def __str__(self) -> str:
        return f' {self.speed} {self.capacity}'
    
    def __repr__(self) -> str:
        return f' {self.speed} {self.capacity}'
    
class Bus(Transport):
    count = 0

    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number
        Bus.count +=1


    def open_door(self):
        return f'Doors open'
    

    @classmethod
    def generate_instances(cls, num):
        instances = []
        for _ in range(num):
            speed = randint(20, 100)
            capacity = randint(1, 250)
            route_number = choice(COMMANDS_NAMES)
            instance = cls(speed, capacity, route_number)
            instances.append(instance)
        return instances
    
    def __str__(self) -> str:
        return f' {self.speed} {self.capacity} {self.route_number}'
    
    def __repr__(self) -> str:
        return f' {self.speed} {self.capacity} {self.route_number}'




class Train(Transport):
    count = 0
    
    def __init__(self, speed, capacity, has_restoran):
        super().__init__(speed, capacity)
        self.has_restoran = has_restoran
        Train.count +=1

    def attach_wagon(self):
        return f'Wagon attached.'
    
    

    @classmethod
    def generate_instances(cls, num):
        instances = []
        for _ in range(num):
            speed = randint(20, 100)
            capacity = randint(1, 250)
            has_restoran = choice([True, False])
            instance = cls(speed, capacity, has_restoran)
            instances.append(instance)
        return instances
    

    def __str__(self) -> str:
        return f' {self.speed} {self.capacity} {self.has_restoran}'
    
    def __repr__(self) -> str:
        return f' {self.speed} {self.capacity} {self.has_restoran}'
    

# def generate_instances(cls, num):
#     instances = []
#     for _ in range(num):
#         instances.append(cls)
#     return instances

def sorting_instances_speed(instances):
    return sorted(instances, key=lambda x: x.speed)


def sorting_instances_capacity(instances):
    return sorted(instances, key=lambda x: x.capacity)




bus = Bus.generate_instances(5)
train = Train.generate_instances(3)

sort_speed = sorting_instances_speed(bus + train)
sort_capacity = sorting_instances_capacity(bus + train)

print(sort_speed)
print(sort_capacity)



# transp1 = Transport.generate_instances(3)
# print(transp1)


