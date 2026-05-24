def raise_to_degrees(numder):
    i = 0
    while True:

        result = numder ** i
        yield result
        if result > 100 * 20:
            return
        i += 1


res = raise_to_degrees(2)
# print(res)
for el in res:
    print(el