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
        self.is_logged = False

    def login(self, card_number, password):
        if card_number == self.card_number and password == self.password:
            self.is_logged = True
            return "Вход выполнен успешно!"
        else:
            return "Неправильный номер карты или пароль!"

    def open_account(self):
        self.balance = 0
        self.is_frozen = False
        return "Открыт новый счет."

    def deposit(self, amount):
        if not self.is_logged:
            return f"Необходимо выполнить вход."
        if not self.is_frozen:
            self.balance += amount
            return f"Счет пополнен на {amount}."
        else:
            return "Счет заморожен. Невозможно совершить операцию."


    def withdraw(self, amount):
        if not self.is_logged:
            return f"Необходимо выполнить вход."
        if not self.is_frozen:
            if self.balance < amount:
                return "Недостаточно средств на счете."
            self.balance -= amount
            return f"Снято со счета: {amount}."
        else:
            return "Счет заморожен. Невозможно совершить операцию."


    def transfer(self, amount, recipient):
        if not self.is_logged:
            return f"Необходимо выполнить вход."
        if not self.is_frozen:
            if self.balance < amount:
                return "Недостаточно средств на счете."
            self.balance -= amount
            recipient.deposit(amount)
            return  f"Перевод {amount} выполнен успешно."
        else:
            return "Счет заморожен. Невозможно совершить операцию."

    def check_balance(self):
        if not self.is_logged:
            return f"Необходимо выполнить вход."
        else:
            return f"Баланс счета: {self.balance}."

    def freeze_account(self):
        if not self.is_logged:
            return f"Необходимо выполнить вход."
        else:
            self.is_frozen = True
            return f"Счет заморожен."

    def change_password(self, new_password):
        if not self.is_logged:
            return f"Необходимо выполнить вход."
        else:
            self.password = new_password
            return f"Пароль успешно изменен."



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
