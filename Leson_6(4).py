
def checker(let1):
    if type(let1) != int:
        raise  TypeError(f"Sorry, we can`t work with {type(let1)}, need only int ")
    else:
        return let1


f_let = "Vasya"
s_let = 6

checker(f_let)
checker(s_let)