from services import gen_consumer, gen_house_list, get_recommendation


def app():
    house_list = gen_house_list(10)
    consumer = gen_consumer
    recs = get_recommendation(consumer=consumer, house_list=house_list)
    return recs