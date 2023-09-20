# - Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
# В этом классе реализуйте метод show_my_drink(), выводящий на печать Газировка и {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза: Обычная газировка. 


class Soda:

    def __init__(self, addition= None):
        self.addition = addition


    def show_my_drink(self):
        if self.addition:
            return f'Газировка и {self.addition}'
        else:
            return f'Обычная газировка'
        
    def __str__(self):
        if self.addition:
            return f'Газировка и {self.addition}'
        else:
            return f'Обычная газировка'

        

soda =Soda('oringe')
print(soda)
