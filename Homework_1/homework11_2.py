# Создайте класс "Транспортное средство", у которого будут атрибуты "скорость", "вместимость" и методы "едь" и "остановись". 
# От этого класса унаследуйте классы "Автобус" и "Поезд", которые будут иметь свои специфические методы и атрибуты, например, метод "открыть двери" и атрибут "номер маршрута" 
# у класса "Автобус". Метод "прицепить вагон" и атрибут "вагон-ресторан" у класса "Поезд".
# В каждом классе реализуйте счетчик экземпляров. Используйте декоратор @classmethod. Создайте функцию, генерирующую заданное кол-во экземпляров класса поезд/автобус и 
# возвращающую список этих экземпляров. Создайте функцию, которая выполнит сортировку экземпляров по переданному параметру "скорость", "вместимость". 
# from operator import attrgetter

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
    
    # def __str__(self) -> str:
    #     return f' {self.speed} {self.capacity}'
    
class Bus(Transport):
    count = 0

    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number
        Bus.count +=1

    def open_door(self):
        return f'Doors open'
    
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
    
    def __str__(self) -> str:
        return f' {self.speed} {self.capacity} {self.has_restoran}'
    
    def __repr__(self) -> str:
        return f' {self.speed} {self.capacity} {self.has_restoran}'
    

def generate_instances(cls, num):
    instances = []
    for _ in range(num):
        instances.append(cls)
    return instances

def sorting_instances_speed(instances):
    return sorted(instances, key=lambda x: x.speed)


def sorting_instances_capacity(instances):
    return sorted(instances, key=lambda x: x.capacity)



bus1 = Bus(90, 50, "A1")
bus2 = Bus(50, 40, "B2")
train1 = Train(60, 500, True)
train2 = Train(80, 400, False)

bus = generate_instances(bus1, 5)
train = generate_instances(train1, 3)

sort_speed = sorting_instances_speed(bus + train)
sort_capacity = sorting_instances_capacity(bus + train)

print(sort_speed)
print(sort_capacity)



