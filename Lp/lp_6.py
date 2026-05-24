
result = []

try:
        data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

        for key in data:
            res = divider(key, data[kem])
            result.append(res)

        print(result)


except TypeError:
        print("TypeError")
        print("Program restarted")

except ZeroDivisionError:
        print("ZeroDivisionError")
        print("Program restarted")

except NameError:
        print("NameError")
        print("Program restarted")