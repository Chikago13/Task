# Создайте класс "Автомобиль", у которого будут свойства "марка", "модель", "год выпуска" и метод "описание", который будет выводить информацию об автомобиле. 
# От этого класса унаследуйте классы "Легковой автомобиль" и "Грузовик", которые будут иметь дополнительные свойства и методы, специфичные для каждого типа автомобиля.


# class Car:

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year


#     def description(self):
#         return f'марка -{self.brand}, модель-{self.model}, год выпуска -{self.year}'
    
# class Passenger_car(Car):

#     def __init__(self, volume):
#         self.volume = volume

#     def body_type(self):
#         pass

# class Truck(Car):

#     def __init__(self, load_capacity):
#         self.load_capacity = load_capacity

#     def trailer(self):
#         pass


# my_car = Car("Audi", "A4", 2023)
# print(my_car.description())


# 2. Создайте класс "Животное", у которого будут свойства "вид", "имя" и метод "звук", который будет возвращать звук, издаваемый животным. От этого класса унаследуйте классы "Собака" и "Кошка", 
# которые будут иметь свои специфические методы и свойства, например, метод "лаять" у собаки и метод "мурлыкать" у кошки.


# class Animal:

#     def __init__(self, view, name, sound):
#         self.view = view
#         self.name = name
#         self.sound = sound


#     def voice(self):
#         return f'Звук, издаваемый животным {self.sound}'  
#         print('Voice')

# class Dog(Animal):

#     def __init__(self, color):
#         self.view = color

#     def bark(self):
#         return f'GAV'  

#     def voice(self):
#         super().voice()
#         print('Guv, Guv, Guv')

# class Cat(Animal):

#     def __init__(self, age, weight):
#         self.age = age
#         self.weight = weight

#     def cat_info(self):
#         return f'{self.age }, {self.weight}'

#     def myr(self):
#         return f'Myr'  


# an = Animal('cat', 'Vie', 'Myu')
# print(an.voice())
# c= Cat(5, 6)
# print(c.myr())
# d = Dog('black')
# print(d.voice())


# 3. Создайте класс "Транспортное средство", у которого будут свойства "скорость", "вместимость" и методы "едь" и "остановись". 
# От этого класса унаследуйте классы "Автобус" и "Поезд", которые будут иметь свои специфические методы и свойства, например, 
# метод "открыть двери" у класса "Автобус" и метод "прицепить вагон" у класса "Поезд".


class Transport_vehicle:

    def __init__(self, speed, capacity):
        self.speed= speed
        self.capacity = capacity


    def go(self):
        return f'the speed was {self.speed}'

    def stop_it(self):
        return f'Stop'

class Bus(Transport_vehicle):

    def info_bus(self):
        return f'скорость- {self.speed}, вместимость - {self.capacity }'

    def open_the_doors(self):
        return f'open_the_doors'



class Train(Transport_vehicle):

    def info_train(self):
        return f'скорость- {self.speed}, вместимость - {self.capacity }'
    

    def attach_the_van(self):
        return f' attach the van'
    

t = Transport_vehicle(100, 150)
print(t.go())
bus = Bus(90, 200)
print(bus.info_bus())