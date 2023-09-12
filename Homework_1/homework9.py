# 1. Создать класс Snow. Класс содержит целое число - количество снежинок.  Класс включает методы перегрузки арифметических операторов сложения, вычитания,   
# умножения и деления. Код этих методов должен выполнять увеличение или уменьшение  количества снежинок на число n или в n раз.   
# Класс также включает метод makeSnow(), который принимает сам объект и число  снежинок в ряду, а возвращает строку вида   
# "*****\n*****\n*****…",  где количество снежинок между '\n' равно переданному аргументу, а количество рядов   
# вычисляется, исходя из общего количества снежинок.

class Snow:

    def __init__(self, num_of_snowflakes: int):
        self.num_of_snowflakes = num_of_snowflakes


    def __add__(self, n):
        return self.num_of_snowflakes + n
    
    def __sub__(self, n):
        return self.num_of_snowflakes - n
    
    def __mul__(self, n):
        return self.num_of_snowflakes * n
    
    def __truediv__(self, n):
        return self.num_of_snowflakes / n
    

    def makeSnow(self, snowflakes_in_row):
        string_of_snowflakes = ''
        row = self.num_of_snowflakes // snowflakes_in_row
        for _ in range(row):
            string_of_snowflakes += '*' * snowflakes_in_row +'\n'
        result = self.num_of_snowflakes -row * snowflakes_in_row
        string_of_snowflakes +='*' * result
        return string_of_snowflakes

    

snow = Snow(5)
print(snow.makeSnow(2))



