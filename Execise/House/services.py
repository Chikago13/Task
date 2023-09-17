from random import randint, choice

from models import House, Consumer
from consts import NAMES, SURNAMES
from annotations import HouseAnnotation, ConsumerAnnotation



def gen_house_list(count: int) -> list[HouseAnnotation]:
    result = []
    for _ in range(count):
        result.append(House(price=randint(10000, 1000000), square=randint(50, 200)))
    return result


def gen_consumer() -> ConsumerAnnotation:
    random_consumer = Consumer(name=choice(NAMES), surname=choice(SURNAMES), account=randint(10000, 1000000))
    return random_consumer



def get_recommendation(consumer: ConsumerAnnotation, house_list: list[HouseAnnotation, ]):
    print(consumer, house_list)
    filter_list = list(filter(lambda x: x.price <=consumer.account, house_list))
    result = sorted(filter_list, key=lambda x: x.square, reverse = True)
    return result
