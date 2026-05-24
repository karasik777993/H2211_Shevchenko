def adder(*args, **kwargs):
    result = 0

    for i in args:
        if type(i) in (int, bool, float):
            result += i
        else:
            try:
                result += float(i)
            except (ValueError, TypeError):
                pass

    for j in kwargs.values():
        if type(j) in (int, bool, float):
            result += j
        else:
            try:
                result += float(j)
            except (ValueError, TypeError):
                pass

    return result


def main():
    print(adder(2, 2))
    print(adder(3.5, 3.5))
    print(adder(3, 4, 5))
    print(adder(a=10, b=11))
    print(adder(1, c=2))
    print(adder(0, -5, 0, a=10))
    print(adder("5", "abc", 10))


if __name__ == "__main__":
    main()