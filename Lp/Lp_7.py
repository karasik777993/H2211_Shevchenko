def generator():
    while True:
        yield "Поворот генератора"


class GeneratorRotator:
    def __init__(self, gen):
        self.gen = gen

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.gen)


gen = generator()
rotator = GeneratorRotator(gen)

for _ in range(5):
    print(next(rotator))