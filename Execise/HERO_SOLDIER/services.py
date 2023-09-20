from random import choice
from consts import COMMANDS_NAMES
from model import Game, Soldier, Hero
from annotations import GameAnnotation, HeroAnnotation, SoldierAnnotation


def creating_team(sold: str) -> list[SoldierAnnotation]:
    com1, com2 = [], []
    for _ in range(sold):
        sold_new = Soldier(stim=choice(COMMANDS_NAMES))
        com1.append(sold_new) if sold_new.stim == 'com1' else com2.append(sold_new)
    return {'com1': {"arm": com1, 'len_arm': len(com1)}, 
            'com2':{"arm": com2, 'len_arm': len(com2)}}


def comparison_of_commands(heroes1: HeroAnnotation, heroes2: HeroAnnotation, arm: list[SoldierAnnotation]):
    her1_level, her2_level = arm['com1']['len_arm'], arm['com2']['len_arm']
    heroes1.level_up(her1_level)
    heroes2.level_up(her2_level)
    if heroes1.level > heroes2.level:
        return f'победил {heroes1}'
    elif heroes1.level < heroes2.level:
        return f'победил {heroes2}'
    else:
        return 'Ничья'