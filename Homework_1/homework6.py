# Написать функцию которая сгенерирует список словарей, где каждый словарь представляет собой запись об ученике (с ключами 'имя', 'возраст', 'оценки'). Далее написать  функцию, которая принимает 
два любых параметра сортировки. Функция осуществляет сортировку переданного списка словарей по двум параметрам, например, если это будет возраст и оценки, сортировка будет выглядеть 
следующим образом:
# Сортируем по возрасту, если возраст у некоторых учеников будет одинаковым, сортируем их по ср.баллу оценок. Первый параметр сортировки является основным.
# !Параметры сортировки передаются в функцию в виде кортежа!


from random import randint
import random


def user_dict(lenlist:int):
    dict_users = []
    list_name = ['Alex', 'Tim', 'Alen', 'Olga', 'Nik', 'Svet', 'Arin', 'Sofia']
    for i in range(lenlist):
        dict_users.append({'name':f'{list_name[randint(0, len(list_name)-1)]}', 'age': randint(15, 20), 'grades':randint(2, 5)}) # [random.randrange(2, 11) for i in range(7)]
    return dict_users

def sort_dict(list_val):
    sorted_user = sorted(list_val, key=lambda x: (x['age'], x['grades']))
    return sorted_user

res = user_dict(10)
# print(res)
print(sort_dict(res))

