# TODO
from cs50 import get_float

Coins = 0
while 1:
    number = get_float('Change owed: ')
    if number > 0:
        break
    else:
        continue
euro = round(number * 100)
while euro > 0:
    if euro >= 25:
        euro = euro - 25
    elif euro >= 10:
        euro = euro - 10
    elif euro >= 5:
        euro = euro - 5
    else:
        euro = euro - 1
    Coins = Coins + 1
print(Coins)