from consts import COMMANDS_NAMES
from random import randint, choice

__all__ = {'Transport', 'Bus', 'Train'}

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
    