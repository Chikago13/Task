# Создайте класс "Банк", у которого есть атрибут "счет" и методы для открытия(0) и закрытия счета(None), а также методы для пополнения и снятия денег со счета. 
# Пополнение и снятие возможно только для открытого счета.

class Bank:

    def __init__(self):
        self.score = {}
        self.close_score = None


    def create_score(self, account_number, initial_balance = 0):
        if account_number in self.score:
            print('Номер счета уже существует.')
        else:
            self.score[account_number]= initial_balance
            print('Учетная запись успешно создана')

    def closing_an_score(self, account_number):
        if account_number in self.score:
            if self.score[account_number]== 0:
                self.score[account_number]= self.close_score
                print('Счет зыкрыт')
            else:
                    print('Выведите средства со счета')
        else:
            print('Счет не существует')



    def replenishment_score(self,account_number, amount):
        if account_number in self.score:
            self.score[account_number] += amount
            print('Счет успешно пополнен')
        else:
            print('Счет не существует')

    def withdrawal_of_money(self,account_number,  amount):
        if account_number in self.score:
            if self.score[account_number] >= amount:
                self.score[account_number] -=amount
                print(f'Вы сняли {amount}')
            else:
                print('Недостаточный баланс')
        else:
            print('Счет не существует')



bank = Bank()
num_score1= "АГ123"
balance1= 1000
print("\n Создание Cчет №.",num_score1, 'Баланс составил',balance1)
bank.create_score(num_score1, balance1)
money1 = 600
print("\n Пополнение",money1,"Cчет №.",num_score1)
bank.replenishment_score(num_score1, money1)
money1 = 1600
print("Вывести",money1,"Счет №.",num_score1)
bank.withdrawal_of_money(num_score1, money1)
bank.closing_an_score(num_score1)
