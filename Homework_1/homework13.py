# Реализовать систему управления банкоматом
# Функция реализации:
# 1. Когда пользователь вводит номер карты и пароль в интерфейсе входа в систему, он может войти в систему;
# 2. Реализуйте функцию открытия счета;
# 3. Взаимодействуйте с машиной, чтобы осуществлять снятие средств, депозиты, переводы и проверку баланса,
# Заморозить аккаунт, сменить пароль и другие функции;

class BankAccount:
    def __init__(self, card_number, password):
        self.card_number = card_number
        self.password = password
        self.balance = 0
        self.is_frozen = False

    def login(self, card_number, password):
        if card_number == self.card_number and password == self.password:
            return "Вход выполнен успешно!"
        else:
            return "Неправильный номер карты или пароль!"

    def open_account(self):
        self.balance = 0
        self.is_frozen = False
        return "Открыт новый счет."

    def deposit(self, amount):
        if self.is_frozen:
            return "Счет заморожен. Невозможно совершить операцию."
        else:
            self.balance += amount
            return f"Счет пополнен на {amount}."

    def withdraw(self, amount):
        if self.is_frozen:
            return "Счет заморожен. Невозможно совершить операцию."
        elif self.balance < amount:
            return "Недостаточно средств на счете."
        else:
            self.balance -= amount
            return f"Снято со счета: {amount}."

    def transfer(self, amount, recipient):
        if self.is_frozen:
            return "Счет заморожен. Невозможно совершить операцию."
        elif self.balance < amount:
            return "Недостаточно средств на счете."
        else:
            self.balance -= amount
            recipient.deposit(amount)
            return  f"Перевод {amount} выполнен успешно."

    def check_balance(self):
        return f"Баланс счета: {self.balance}."

    def freeze_account(self):
        self.is_frozen = True
        return "Счет заморожен."

    def change_password(self, new_password):
        self.password = new_password
        return "Пароль успешно изменен."


account = BankAccount("1234567890", "password")
print(account.login("1234567890", "password"))
print(account.open_account())
print(account.deposit(1000))
print(account.check_balance())
print(account.withdraw(500))
print(account.check_balance())
recipient = BankAccount("0987654321", "password")
print(account.transfer(300, recipient))
print(account.check_balance())
print(recipient.check_balance())
print(account.change_password("new_password"))

