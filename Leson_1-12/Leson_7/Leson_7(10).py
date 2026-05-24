try:

    class Counter:
        def __init__(self, max_string):
            self.i = "a"
            self.max_string = max_string


        def __iter__(self):
            self.i = "a"
            return self

        def __next__(self):
            self.i += "b"
            if self.i > self.max_string:
                raise StopIteration
            return self.i

    count = Counter(5)
    for str in count:
        print(str)

except TypeError:
    print("TypeError")
except IndentationError:
    print("IndentationError")