# Реализовать паттерн итератор. 

class Client:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class ClientIterator:

    def __init__(self, client):
        self.client = client
        self.index = 0


    def __iter__(self):
        return self
    

    def __next__(self):
        
        if self.index >=len(self.client):
            raise StopIteration
        client = self.client[self.index]
        self.index +=1
        return client
        
clients = Client("John", 25), Client("Alice", 30), Client("Bob", 35)
client_iterator = ClientIterator(clients)

for client in client_iterator:
    print(client.name, client.age)
