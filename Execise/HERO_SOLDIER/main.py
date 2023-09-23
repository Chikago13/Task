from services import creating_team, comparison_of_commands
from model import Game, Soldier, Hero


def app():
    solder = Soldier('start')
    heroes1 = Hero('com1')
    heroes2 = Hero('com2')
    creat_team = creating_team(50)
    recs = comparison_of_commands(heroes1, heroes2, creat_team)
    res = solder.go_to_hero(heroes1)
    return recs, res


print(app())