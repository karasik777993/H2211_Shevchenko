import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.hungry = 0
        self.stuffed = 50
        self.cheerful = 50
        self.cat_alive = True

    def to_eat(self):
        print("Time eat")
        self.hungry -= 15
        self.stuffed += 5
        self.gladness += 2

        if self.hungry < 0:
            self.hungry = 0

    def to_sleep(self):
        print("I will sleep")
        self.cheerful += 5
        self.hungry += 5
        self.gladness += 2

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.hungry += 7

    def is_cat_alive(self):
        if self.hungry >= 100:
            print("Cat died from hunger...")
            self.cat_alive = False

        elif self.gladness <= 0:
            print("Cat depression...")
            self.cat_alive = False

        elif self.stuffed <= 0:
            print("Cat died from exhaustion...")
            self.cat_alive = False

        elif self.gladness >= 90 and self.cheerful >= 90:
            print("The cat has a great owner!")
            self.cat_alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Hungry = {self.hungry}")
        print(f"Cheerful = {self.cheerful}")
        print(f"Stuffed = {self.stuffed}")


    def live(self, day):
        day = f"Day {day} of {self.name} life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        else:
            print("Nothing happens")
        self.end_of_day()
        self.is_cat_alive()



cat = Cat(name="Vasya")

for day in range(365):
    if not cat.cat_alive:
        break
    cat.live(day)