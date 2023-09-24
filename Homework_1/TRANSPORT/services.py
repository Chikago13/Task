from model import Transport, Bus, Train
from annotations import TransportAnnotation, BusAnnotation, TrainAnnotation


def sorting_instances_speed(instances: list[TransportAnnotation]):
    return sorted(instances, key=lambda x: x.speed)


def sorting_instances_capacity(instances: list[TransportAnnotation]):
    return sorted(instances, key=lambda x: x.capacity)