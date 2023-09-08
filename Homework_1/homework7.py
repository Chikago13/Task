# Создать класс Human c атрибутами name, surname, birth_year и двумя методами full_name(), который будет  возвращать полное имя: Name Surname и get_age(), 
# возвращающий возраст, созданного экземпляра 

from datetime import datetime


class Human:
    name: str
    surname:str
    birth_year: int
    
    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year


    def full_name(self):
        return f'Имя: {self.name} Фамилия: {self.surname}'
    
    def get_age(self):
        return f' Возраст человека: {datetime.now().year-self.birth_year}'

human_1 = Human('Alex', 'Volkov', 1988)

print(human_1.full_name())
print(human_1.get_age())


# Доп. задачи:
# 1. Напишите функцию, преобразующую строку в CamelCase:
# "the-stealth-warrior"преобразуется в"theStealthWarrior" 
# "The_Stealth_Warrior"преобразуется в"TheStealthWarrior" 
# "The_Stealth-Warrior"преобразуется в"TheStealthWarrior"


# def CamelCase(st):
#     return st[0] + st.title()[1:].replace('-', '').replace('_','')

# print(CamelCase("the-stealth-warrior" ))
# print(CamelCase("The_Stealth_Warrior" ))
# print(CamelCase("The_Stealth-Warrior" ))

# 2. Напишите функцию, которая принимает массив из 10 целых чисел (от 0 до 9) и возвращает строку этих чисел в виде номера телефона. 
# Пример: 
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-78-90"

def create_phone_number(n):
    return '('+''.join(map(str, n[0:3]))+')'+''+''.join(map(str, n[3:6]))+'-'+''.join(map(str, n[6:]))

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
