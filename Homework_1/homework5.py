# Реализовать функцию игры "Камень, ножницы, бумага" для двух игроков.
# Функция принимает две строки, каждая из которых обозначает один из предметов: "камень", "ножницы", "бумага" и возвращает тот предмет, который является победителем, например:
# game("rock", "paper") - > paper is winner.

def games():
    while True:
        player1 = input('Player1 Введите: rock, paper, scissors, exit - для выхода ')
        if player1 == 'exit':
            break
        player2 = input('Player2 Введите: rock, paper, scissors, exit - для выхода ')
        if player2 == 'exit':
            break
        if player1 == 'rock':
            if player2 == 'rock':
                return 'draw'
            elif player2 == 'paper':
                return 'player2 winner'
            elif player2 == 'scissors':
                return 'player1 winner'
            else:
                raise Exception(f"Некорректные данные")
        elif player1 == 'paper':
            if player2 == 'rock':
                return 'player1 winner'
            elif player2 == 'paper':
                return 'draw'
            elif player2 == 'scissors':
                return 'player2 winner'
            else:
                raise Exception(f"Некорректные данные")
        elif player1 == 'scissors':
            if player2 == 'rock':
                return 'player2 winner'
            elif player2 == 'paper':
                return 'player1 winner'
            elif player2 == 'scissors':
                return 'draw'
            else:
                raise Exception(f"Некорректные данные")
        else:
            raise Exception(f"Некорректные данные")
        
print(games())
            



