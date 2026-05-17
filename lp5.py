import colorama
import inspect
import sys


for component in dir(__builtins__):
    print(component)


for module_nam, module_path in sys.modules.items():
    print(module_nam, module_path)

print(sys.executable)
print(sys.version)

print(sys.executable)
print(sys.version)
print(inspect.isfunction(colorama))
print(inspect.isclass(colorama))
print(inspect.ismodule(colorama))
print(inspect.getmodule(list))