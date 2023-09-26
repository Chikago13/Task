from model import Transport, Bus, Train
from services import sorting_instances_capacity, sorting_instances_speed

def app():
    bus = Bus.generate_instances(5)
    train = Train.generate_instances(3)
    sort_speed = sorting_instances_speed(bus + train)
    sort_capacity = sorting_instances_capacity(bus + train)
    return sort_speed, sort_capacity


print(app())