import requests
import inspect

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))