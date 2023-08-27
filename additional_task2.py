

# 1.Напишите программу, которая выводит на экран все числа от 1 до 10.

# def funck_range():
#     return [i for i in range(1, 11)]

# print(funck_range())

# 2. Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран все числа от 1 до n.

# def funck_us():
#     a = int(input('Введите число:'))
#     return [ i for i in range(1, a)]

# print(funck_us())

# 3. Напишите программу, которая выводит на экран все четные числа от 2 до 20

# def even_numbers():
    # return [ i for i in range(2, 20) if i % 2==0]

    # count = []
    # for i in range(2, 20):
    #     if i % 2 == 0:
    #         count.append(i)
    # return count

# print(even_numbers())

# 4. Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран все четные числа от 2 до n.

# def user_n():
#     n = int(input('Введите число:'))
#     return [i for i in range(2, n) if i % 2 == 0]

# print(user_n())

# 5. Напишите программу, которая выводит на экран таблицу умножения от 1 до 10.


# def multiplication_table():
    # return [[i * j for j in range(1, 11)] for i in range(1, 11)]
#     res= ''
#     for i in range(1, 11):
#         for j in range (1, 11):
#             res += f'{i*j}\t' #\t у нас появился отступ
#         res += f'\n'
#     return res


# print(multiplication_table())
    

# 6. Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран таблицу умножения от 1 до n.

# while True:
#     n =input('Введите число или q для выхода из программы:')

#     if n == 'q':
#         break
#     else:
#         num = int(n)
#         for i in range(1, num):
#             print(f'{num}* {i}= {num*i}')

# 7. Напишите программу, которая запрашивает у пользователя число n, а затем выводит на экран все числа от n до 1 в обратном порядке.

# def user_num():
#     n = int(input('Введите число:'))
#     return str(n)[::-1]

# print(user_num())

# 8.Напишите программу, которая выводит на экран все буквы английского алфавита.

# for i in range(65, 91):
#     print(chr(i) + chr(i + 32) + ' ', end='') # chr  символов Unicode

# 9. Напишите программу, которая запрашивает у пользователя слово, а затем выводит на экран все буквы этого слова в обратном порядке.

# def user_word():
#     n = input('Введите слово:')
#     return n[::-1]


# print(user_word())

# def user_word(n):
#     if len(n) == 0:
#         return n
#     else:
#         return user_word(n[1:]) + n[0]
    

# a = str(input("Введите строку: "))
# print(user_word(a))

# 10. Напишите программу, которая запрашивает у пользователя слово, а затем выводит на экран все буквы этого слова, кроме буквы "а".

# def user_word():
#     word = str(input("Введите слово: "))
    # return [i for i in word if 'a' not in i]
#     res = ''
#     for i in word:
#         if i not in 'a':
#             res += i
#     return res


# print(user_word())
