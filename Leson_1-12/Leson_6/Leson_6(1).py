try:
    print("start code")
    print(10/0)
    print("No error")
except ZeroDivisionError:
    print("We have an error")
except NameError:
    print("Sorry")
print("code after cap")

