import requests

def first_func():
    pass

class Human:
    pass

rq = requests
first_f = first_func
nick = Human




print(requests.__name__)
print(rq.__name__)
print(first_func.__name__)
print(first_f.__name__)
print(Human.__name__)
print(nick.__name__)

for method in dir():
    print(method)