#  Создать класс Robot 
# Класс инициализируется начальными координатами – положением Робота на  
# плоскости, обе координаты заключены в пределах от 0 до 100.  
# Робот может передвигаться на одну клетку вверх (N), вниз (S), вправо (E), влево (W).  
# Выйти за границы плоскости Робот не может.  
# Метод move() принимает строку – последовательность команд перемещения робота,  
# каждая буква строки соответствует перемещению на единичный интервал в направлении,  
# указанном буквой. Метод возвращает список координат – конечное положение Робота  
# после перемещения

# class Robot:

#     def __init__(self, x, y):
#         if x not in range(0, 101):
#             print('Несоответсвует кординате x:')
#             exit(0)
#         if y not in range(0, 101):
#             print('Несоответсвует кординате y:')
#             exit(0)
#         self.x =x
#         self.y = y
#         # self.x = x if x not in range(0, 101) else 0
#         # self.y = y if y not in range(0, 101) else 0


#     def move(self, res):
        
#         # self.x = max(0, min(self.x, 100))
#         # self.y = max(0, min(self.y, 100))

#         for  i in res:

#             if i == 'N':
#                 if self.y+1 not in range(0, 101):
#                     return 'Несоответсвует кординате y:'
#                 self.y += 1
                
            
#             if i == 'S':
#                 if self.y-1 not in range(0, 101):
#                     return 'Несоответсвует кординате y:'
#                 self.y -= 1

#             if i == 'E':
#                 if self.x+1 not in range(0, 101):
#                     return 'Несоответсвует кординате x:'
#                 self.x += 1
            
#             if i == 'W':
#                 if self.x-1 not in range(0, 101):
#                     return 'Несоответсвует кординате x:'
#                 self.x -= 1



#         return self.x, self.y


# r= Robot(0, 0)
# print(r.move('NNEWS'))


class Robot:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self, commands):
        count = 0

        while count < len(commands):
            # print(commands)
            command = commands[count]
            if command == 'N':
                if self.y < 100:
                        self.y += 1
                elif command == 'S':
                    if self.y > 0:
                        self.y -= 1
                elif command == 'E':
                    if self.x < 100:
                        self.x += 1
                elif command == 'W':
                    if self.x > 0:
                        self.x -= 1
            count += 1

        return self.x, self.y


r= Robot(0, 0)
print(r.move('NNEWS'))