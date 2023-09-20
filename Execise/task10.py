# В  некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У 
# солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня. 
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется 
# случайно. Солдаты разных команд добавляются в разные списки. Измеряется длина списков 
# солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, увеличивается уровень. 
# Отправляем одного из солдат следовать за первым героем и выводим их идентификационные номера.
from random import choice, randint

__all__ = {'Person', 'Heroes', 'Soldier'}
COMMANDS_NAMES = ['com1', 'com2']

class Person:
    TOTAL = 1

    def __init__(self, stim):
        self.id = Person.TOTAL
        self.stim = stim
        Person.TOTAL +=1


class Heroes(Person):

    def __init__(self, stim, level = 1):
        super().__init__(stim)
        self.level = level

    def level_up(self, res):
        self.level += res

    def __str__(self):
        return f'{self.level} , {self.stim}'
    


class Soldiers(Person):
    

    def go_to_hero(self, hero):
        # return f'Следую за героем {choice(str(self.id))} команды {hero.stim}'
        return f'Следую за героем {randint(1, self.id)} команды {hero.stim}'


def game(sold):
    com1, com2 = [], []
    for _ in range(sold):
        sold_new = Soldiers(stim=choice(COMMANDS_NAMES))
        com1.append(sold_new) if sold_new.stim == 'com1' else com2.append(sold_new)
    return {'com1': {"arm": com1, 'len_arm': len(com1)}, 
            'com2':{"arm": com2, 'len_arm': len(com2)}}


def var(heroes1, heroes2, arm):
    her1_level, her2_level = arm['com1']['len_arm'], arm['com2']['len_arm']
    heroes1.level_up(her1_level)
    heroes2.level_up(her2_level)
    if heroes1.level > heroes2.level:
        return f'победил {heroes1}'
    elif heroes1.level < heroes2.level:
        return f'победил {heroes2}'
    else:
        return 'Ничья'


heroes1 = Heroes('com1')
heroes2 = Heroes('com2')

gam = game(50)
print(gam)
print(var(heroes1, heroes2, gam))



p1= Person('start')
# p2= Person('start')
# print(p1.id)
# print(p2.id)
s = Soldiers('starr')
print(s.go_to_hero(heroes1))
