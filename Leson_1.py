class Stident:
    def __init__(self, h=160):
        self.h = h


nick = Stident()
rimuru = Stident(h=170)

print(nick.h)
print(rimuru.h)