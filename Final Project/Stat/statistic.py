# library
import sys
import calculator 

# main function
def main():
    x = [1, 2, 3, 2,53,53,5,3,5,3,5,3,2]
    print(meann(x))



# Sum of Number in List
def summ(x):
    if type(x) != list:
        print('should type x is list!')
        exit()
    for i in range(len(x)):
        if type(x[i]) != int and type(x[i]) != float:
            print('should type x is intiger or float!')
            exit()
    
    y = 0
    for i in range(len(x)):
        if i == 0:
            y = x[i]
        else:
            y = y + x[i]
    return y


# Average Number in List
def meann(x):
   return summ(x) / len(x)


# Variance Number in List
def varr(x):
    if type(x) != list:
        print('should type x is list!')
        exit()
    for i in range(len(x)):
        if type(x[i]) != int and type(x[i]) != float:
            print('should type x is intiger or float!')
            exit()
    y = []
    for i in range(len(x)):
        y.append((x[i] - meann(x)) ** 2)
    return summ(y) / (len(x) - 1)

# Standard deviation from the mean
def sdd(x):
    return (varr(x) ** 0.5)

def mediann(x):
    if type(x) != list:
        print('should type x is list!')
        exit()
    for i in range(len(x)):
        if type(x[i]) != int and type(x[i]) != float:
            print('should type x is intiger or float!')
            exit()
    
    
    x = sorted(x)
    if calculator.cmath('remainder', [len(x), 2]) == 0:
        return (x[int(calculator.cmath('/', [len(x), 2])) - 1] + x[int(calculator.cmath('/', [len(x), 2]))]) / 2
    else:
        x[int(calculator.cmath('/', [len(x), 2])) - 1]
        return x[round(calculator.cmath('/', [len(x), 2])) - 1]


def modee(x):
    if type(x) != list:
        print('should type x is list!')
        exit()
    for i in range(len(x)):
        if type(x[i]) != int and type(x[i]) != float:
            print('should type x is intiger or float!')
            exit()
    table = {}
    for i in range(len(x)):
        table[x[i]] = 0
        for j in range(len(x)):
            if x[i] == x[j]:
                table[x[i]] += 1
                
    return max(table, key=table.get)


def skewness(x):
    if type(x) != list:
        print('should type x is list!')
        exit()
    for i in range(len(x)):
        if type(x[i]) != int and type(x[i]) != float:
            print('should type x is intiger or float!')
            exit()

    m = meann(x)
    y1 = []
    y2 = []
    for i in range(len(x)):
        y1.append((x[i] - m) ** 3)
        y2.append((x[i] - m) ** 2)
    sy1 = summ(y1)
    sy2 = summ(y1)

    s = (sy1 / len(x)) / ((sy2 / (len(x) - 1)) ** (3 / 2))
    if s > 0:
        print('Skewness to the Right.')
        return s
    elif s < 0:
        print('Skewness to the Left.')
        return s
    else:
        print('There is no skewness.')
        return s
    
def kurtosis(x):
    if type(x) != list:
        print('should type x is list!')
        exit()
    for i in range(len(x)):
        if type(x[i]) != int and type(x[i]) != float:
            print('should type x is intiger or float!')
            exit()

    m = meann(x)
    y1 = []
    y2 = []
    for i in range(len(x)):
        y1.append((x[i] - m) ** 4)
        y2.append((x[i] - m) ** 2)
    sy1 = summ(y1)
    sy2 = summ(y2)

    return ((sy1 / len(x)) / ((sy2 / len(x)) ** 2)) - 3


# Exit Programm
def exit():
    sys.exit(0)


if __name__ == '__main__':
    main()