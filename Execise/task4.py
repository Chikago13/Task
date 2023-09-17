
# 2. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий только те строки, которые начинаются с буквы 'a' (большой или малой).

# def string_a(a: list[str]):
#     return [ i for i in a if i.startswith('a') or i.startswith('A') ]

# print(string_a(['apple', 'Answer', 'type', 'ask']))

# 3. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий только те числа, которые больше среднего значения всех чисел в списке.

# def list_s(sp):
#     count = sum(sp)/len(sp)
#     res = []
#     for i in sp:
#         if i>count:
#             res.append(i)
#     return res

# print(list_s([1, 54, 656, 77, 454]))

# 4. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий те же строки, но с замененным первым символом на символ '*' (например, "hello" станет "*ello").

# def list_st(st):
    # return list(map(lambda x: '*'+ x[1:], st))
    # res = []
    # for i in st:
    #     i = '*'+ i[1:]
    #     res.append(i)
    # return res


# print(list_st(['hello', 'age', 'word', 'milk']))

# def string_s(st):
#     res = ''
#     center = int((len(st)-1) / 2)
#     if len(st)% 2== 0:
#         return st[center: center +2]
#     return st[center]
    
# print(string_s('apple'))



