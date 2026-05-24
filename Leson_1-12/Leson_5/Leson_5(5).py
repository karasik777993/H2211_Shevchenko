import sys
import requests

for module_nam, module_path in sys.modules.items():
    print(module_nam, module_path)