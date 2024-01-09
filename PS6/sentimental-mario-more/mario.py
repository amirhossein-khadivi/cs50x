# TODO
from cs50 import get_int
while 1:
    height = get_int('Height: ')
    if height > 8 or height < 1:
        print('Height is should among 1 to 8 ')
        continue
    else:
        break
for a in range(height):
    print((height - (a + 1)) * ' ' + (a + 1) * '#' + '  ' + (a + 1) * '#')