

# ДОП. ЗАДАЧИ НА ФУНКЦИИ
# 1. Напишите функцию, которая принимает список чисел и возвращает список квадратов этих чисел. 

# def funck_skv(sp):
#     return [i**2  for i in sp]

# print(funck_skv([2, 3, 5, 6]))


# 2. Напишите функцию, которая принимает на вход список строк и возвращает список строк, длина которых больше 5 символов. 

# def funck_string(word):
#     return [i for i in word if len(i)>=5]
    # res = []
    # for i in word:
    #     if len(i)>=5:
    #         res.append(i)
    # return res

# print(funck_string(['Hello', 'apple', 'queer', 'the', 'four', 'friends', 'are']))

# 3. Напишите функцию, которая принимает на вход список чисел и возвращает только четные числа из этого списка. 

# def even_numb(numb):
#     return [i for i in numb if not i % 2 ]

# print(even_numb([2, 3, 6, 9, 21, 14, 54, 34, 78]))

# 4. Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов четных чисел из этого списка. 

# def even_numb(numb):
#     return [i**2 for i in numb if not i % 2 ]


# print(even_numb([2, 3, 6, 9, 21, 14, 54, 34, 78]))

# 5. Напишите функцию, которая принимает на вход список строк и возвращает список строк, которые начинаются с буквы "a". 

# def funck_a(letter):
    # return [i for i in letter if i[0] in 'a']
#     res = []
#     for i in letter:
#         if i in 'a':
#             res.append(i)
#     return res


# print(funck_a(['Hello', 'apple', 'queer', 'the', 'four', 'friends', 'are']))

# 6. Напишите функцию, которая принимает на вход список чисел и возвращает список чисел, которые больше 10 и меньше 20. 

# def funck_list(ls):
#     return [ i for i in ls if 10<i<20]
    # res = []
    # for i in ls:
    #     if 10<i<20:
    #         res.append(i)
    # return res

# print(funck_list([1, 5, 10, 11, 350, 19, 22, 15]))

# 7. Напишите функцию, которая принимает на вход список строк и возвращает список строк, которые содержат букву "e". 

# def funck(ls):
#     return [ i for i in ls if 'e' in i]

# print(funck(['hello', 'may', 'bye', 'friend']))

# 8. Напишите функцию, которая принимает на вход список чисел и возвращает True, если все числа в списке положительные, и False в противном случае. 

# def number(num):
#     for i in num:
#         if i > 0:
#             result = True
#         else:
#             result = False
#             break
#     return result

# print(number([1, 2, 3]))

# 9. Напишите функцию, которая принимает на вход список строк и возвращает список строк, которые содержат только цифры. 

# def funck(st):
#     return list(filter(lambda x: isinstance(x, int), st))

# print(funck(['df', 4, 45, '43', 78, 'hello']))

# 10. Напишите функцию, которая принимает на вход список чисел и возвращает список чисел, которые являются степенями двойки.

# def funck_ls(ls):
    # count = []
    # for i in ls:
    #     if i > 0 and (i & (i - 1)) == 0:
    #         count.append(i)
    # return count




# print(funck_ls([1, 2, 4, 5, 6, 8, 12, 16]))


