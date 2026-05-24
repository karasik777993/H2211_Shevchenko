try:
    print("start code")
    print(10/0)
    print("No error")
except (ZeroDivisionError, NameError):
    print("We have an error")
print("code after cap")
