def raise_to_degrees(numder,max_degree):
    i = 0
    for _ in range(max_degree):
        yield numder ** i
        i += 1


res = raise_to_degrees(2, 2)
# print(res)
for el in res:
    print(el)