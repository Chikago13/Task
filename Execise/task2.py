import random
from sympy import isprime

def random_list(count: int):
    return [ random.randint(0, 100) for _ in range(count)]

def is_num(count):
    return [i for i in count if isprime(i)]
    # res = []
    # for i in count:
    #     if isprime(i):
    #         res.append(i) 
    # return res 


def res_num(list_num):
    return f" Простые числа: {list_num}"








# print(random_list(20))
# print(is_num([88, 94, 22, 22, 41, 4, 52, 91, 2, 78, 38, 4, 28, 5, 0, 62, 54, 87, 86, 30]))
print(res_num(is_num(random_list(20))))

