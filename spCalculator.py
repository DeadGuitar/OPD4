
def spcalc(deposit, time, interest):
    if not ((isinstance(deposit, float) or isinstance(deposit, int)) and isinstance(time, int) and
            (isinstance(interest, int) or isinstance(interest, float))):
        raise TypeError("Wrong input type used")
    if deposit < 0 or time < 0 or interest < 0:
        raise ValueError("Wrong input value")
    ans = deposit
    for payment in range(time):
       ans += round(ans*(interest/1200), 2)
    return round(ans, 2)

