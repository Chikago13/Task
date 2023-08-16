import datetime


# 1.Создать функцию, которая принимает список чисел и возвращает новый список, состоящий из квадратов чисел, которые больше 10.

# def func(a):
#     return [i**2 for i in a if i**2>10]


# print(func([1, 2, 3, 5, 8, 7, 6]))

# 2. Написать функцию, которая принимает список строк и сортирует их по возрастанию длины каждой строки.

# def func_sort(a):
#     return sorted(a, key=len)


# print(func_sort(['aaa', 's', 'sdfsadf', 'asds']))

# 3*. Написать функцию, которая принимает дерево, представленное в виде списка списков, где каждый элемент списка может быть либо числом, либо подсписком, и возвращает сумму всех чисел в дереве.

def func_list(a):
    sum = 0
    for i in a:
        if isinstance(i, list):
            for j in i:
                sum += j
        else:
            sum+=i
    return sum


print(func_list([5, 12, [1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# 4. Написать функцию, которая принимает список дат в формате 'ДД.ММ.ГГГГ' и возвращает список дат в формате 'ГГГГ-ММ-ДД', отсортированный по возрастанию.
# strptime() принимает в качестве одного из аргументов строку и создает на основе её объект типа datetime. 
# strftime() преобразует объект типа datetime в строку. 

# def func_date(a):
#     s_date=sorted([datetime.datetime.strptime(i, '%d.%m.%Y') for i in a])
#     return [i.strftime('%Y.%m.%d') for i in s_date]


# print(func_date(['20.01.1990', '01.05.2020', '31.12.2022']))


# Написать программу, которая будет конвертировать строку в CamelCase. Например: 
# "the-stealth-warrior" -> "theStealthWarrior"  
# "The_Stealth_Warrior" -> "TheStealthWarrior"  
# "The_Stealth-Warrior" -> "TheStealthWarrior"



def CamelCase(st):
    return st[0]+st.title()[1:].replace("-","").replace("_","")

def CamelCase(st):
    res = st.replace("-", " ").replace("_", " ")
    res = res.split()
    if len(st) == 0:
        return st
    return res[0] + ' '.join(res[1:]).title().replace(" ", "")

print(CamelCase("the-stealth-warrior" ))
print(CamelCase("The_Stealth_Warrior" ))
print(CamelCase("The_Stealth-Warrior" ))



