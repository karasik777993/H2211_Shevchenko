
class PeopleError(Exception):
    def __str__(self):
        return f"Bad name!"

def check_people(human_name, limit_value):
    if human_name == "Illa":
     return "bad name"
    else:
        raise PeopleError(human_name)




human_name ="Vasya"

check_people(human_name, "Vasya")