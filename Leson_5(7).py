import random
import inspect
import sys

for component in dir(__builtins__):
    print(component)

for module_nam, module_path in sys.modules.items():
    print(module_nam, module_path)

print(sys.executable)
print(sys.version)
print(inspect.isfunction(random))
print(inspect.isclass(random))
print(inspect.ismodule(random))
print(inspect.getmodule(random.getrandbits))
print(inspect.getmodule(list))