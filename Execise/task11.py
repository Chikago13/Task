
# Bugs with late binding closure
# You have a function that takes an integer n and returns a list of length n of function objects that take an integer x and return x multiplied by the index of that 
# object in this list(remember that in python the indexes of elements start from 0):


def create_multiplications(n):
    return [lambda x, i=i: i * x for i in range(n)]

# fixme: Hello
# The code provided has a method hello which is supposed to show only those attributes which have been explicitly set. 
# Furthermore, it is supposed to say them in the same order they were set. But it's not working properly.
# Notes
# There are 3 attributes
# name
# age
# sex ('M' or 'F')
# When the same attribute is assigned multiple times the hello method shows it only once. 
# If this happens the order depends on the first assignment of that attribute, but the value is from the last assignment.


class Dinglemouse(object):
    
    def __init__(self):
        self.res = {}
    
    def setAge(self, age):
        self.res['age']=f'I am {age}.'
        return self
        
    def setSex(self, sex):
        self.res['sex']=f'I am {"male" if sex=="M" else "female"}.'
        return self
        
    def setName(self, name):
        self.res['name']=f'My name is {name}.'
        return self
        
    def hello(self):
        return ' '.join(['Hello.'] + list(self.res.values()))
    
