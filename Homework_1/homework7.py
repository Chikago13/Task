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

