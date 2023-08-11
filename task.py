# a = float(input('Введите число от 1 до 12'))

# if a not in  range(1, 13):
#     print('Введите правильное число')
#     exit(0)

# if a in (12, 1, 2):
#     print('Зима')
# elif a in (9, 10, 11):
#     print('Осень')
# elif a in (6, 7, 8):
#     print('Лето')
# else:
#     print('Весна')


# 1. Написать программу, которая удаляет первый и последний символы строки. Если строка содержит меньше  двух символов - вывести сообщение об ошибке. 

# string = "Hello"
# if len(string)<2:
#     print('Ошибка')
# else:
#     print(string[1:-1])

# 3. Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.   

# list1 = ['ask', 'bel', 'hello', 'car', 'cool', 'python']
# list2 = ['ask', 'car', 'cool']

# print([i for i in list1 if i not in list2])



# 4. Создайте простой калькулятор, который считывает из строки ввода(пример: «1 + 13» три подстроки: 1-ое число, 2-ое число и операцию, после чего применяет операцию к введённым числам, а затем выводит результат на экран. 

# while True:
#     operator = input('Введите операцию (+, -, *, /,):')
#     if operator == 'exit':
#         break
#     num1=float(input('Введите первое число: '))
#     num2=float(input('Введите второе число: '))
#     if operator == '+':
#         print(num1+num2)
#     if operator == '-':
#         print(num1-num2)
#     if operator == '*':
#         print(num1*num2)
#     if operator == '/':
#         try:
#             print(num1/num2)
#         except ZeroDivisionError as e:
#             print(f'Ошибка: {e}')

# 5.Вы вводите с клавиатуры последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.

a = input('Введите последовательность чисел, разделённых запятой:')

list = a.split(',')
tuple = tuple(list)
print(list)
print(tuple)