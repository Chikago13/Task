# 1. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий те же числа, но отсортированные по возрастанию. 

# def list_int(ls):
#     return sorted(ls)

# print(list_int([1, 43, 5, 4, 23, 12]))

# 2. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий только те строки, которые состоят только из букв (верхнего или нижнего регистра). 

# def list_st(st):
#     return [ i for i in st if i.isalpha()]

# print(list_st(['hello', '42344', 'dsaf34', 'ask', 'Lif']))

# 3. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий только те числа, которые делятся на 3 без остатка. 

# def list_int(ls):
#     return [i for i in ls if i%3==0]

# print(list_int([3, 4,  6, 9, 27, 18, 2, 8,]))

# 4*. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, содержащий только те числа, которые являются простыми. 

# def list_num(num):
#     if num < 2: 
#         return False
#     for i in range(2, int(num ** 0.5) + 1): 
#         if num % i == 0: 
#             return False 
#         return True
    
# def filter_num(a, b):
#     return list(filter(b, a))

# print(filter_num([1, 2, 65, 5, 3, 78, 85, 11, 53, 47, 61], list_num))

# 5. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий только те строки, которые длиннее 5 символов. 

# def list_str(st):
#     return [i for i in st if len(i)>5]
    # return list(filter(lambda x: len(x)>5, st))

# print(list_str(['hello', 'ask', 'what', 'friend', 'return']))

# 6. Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий только те строки, которые содержат хотя бы одну цифру. 

# def list_st(st: list[str]):
    # return [ i for i in st for j in i if j.isdigit()]
#     count = []
#     for i in st:
#         for j in i:
#             if j.isdigit():
#                 count.append(i)
#     return count

# print(list_st(['hello', 'ask523', '258', 'try', '24pip']))


# 7.Напишите функцию, которая принимает на вход список строк и возвращает новый список, содержащий те же строки, но в верхнем регистре.

# def list_str(st):
#     # return list(map(str.lower(), st))
#     return [i.upper() for i in st]

# print(list_str(['hello', 'ask', 'what', 'friend', 'return']))

