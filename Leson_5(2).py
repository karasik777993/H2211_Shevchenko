import inspect
import random

import requests

print(inspect.isfunction(requests))
print(inspect.isclass(requests))
print(inspect.ismodule(requests))

print(inspect.getmodule(random.getrandbits))
print(inspect.getmodule(list))