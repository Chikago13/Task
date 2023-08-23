import re
from collections import defaultdict

# 1. Напишите функцию, которая принимает на вход список строк и возвращает наиболее часто встречающуюся строку.

# def invert(l):
#     res = defaultdict(int)
#     for i in l:
#         res[i] += 1
#     return res


# print(invert(['sddsa', 'sd', 'sd', 'adgre', 'sd']))

# 2.Напишите функцию, которая принимает на вход два списка и возвращает новый список, содержащий элементы, которые есть в обоих списках. 

# a = [1, 2, 3, 4]
# b = [5, 6, 7]


# def funck_list(a, b):
#     res = [a, b]
#     return [i for j in res for i in j]


# print(funck_list(a, b))

# 3. Напишите функцию, которая принимает на вход строку и возвращает количество слов в этой строке, в которых есть более 3-х гласных (a, e, i, o, u)

# def vowel_words(string):
#     vowel = ['a','e','i','o','u']
#     res = 0
#     for i in string:
#         if i in vowel:
#             res += 1 
#     return res

# def vowel_words(string):
#     vowel = r"\b[\w]*[aeiou]{3,}[\w]*"
#     result = re.findall(vowel, string)
#     return result


# print(vowel_words('hello word the queen '))

# 4.Написать функцию, которая принимает список словарей, где каждый словарь представляет собой запись об ученике (с ключами 'имя', 'возраст', 'оценки'), и возвращает список словарей, отсортированный по возрасту учеников.

# dict_list = [
#     {'name' : 'Alex', 'age' : 30, 'evaluations': '5, 4, 5'}, 
#     {'name' : 'Alen', 'age' : 25, 'evaluations': '5, 4, 4'}, 
#     {'name' : 'Tim', 'age' : 40, 'evaluations': '4, 4, 4'}
#     ]

# def funck_dict(a):
#     sort_dict = sorted(dict_list, key=lambda i: i['age'])
#     return sort_dict

# print(funck_dict(dict_list))