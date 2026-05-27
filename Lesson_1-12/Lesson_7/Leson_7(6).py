class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self,work):
        return f"I wiil help you with {self.work} Afterwards I will help you with {work}"


helper = Helper("Homework")
print(helper("Cleaning"))