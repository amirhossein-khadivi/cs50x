import sys
import statistic

def main():
    x1 = [1, 2, 4]
    x2 = [1, 3, 3]
    print(pearson(x1, x2))

def pearson(x1 = None, x2 = None):
    if x1 == None :
        while True:
            try:
                print('Should lenght x1 & x2 equal!')
                num = int(input('Enter Num x1: '))
                break
            except:
                print('Should Num x1 is intiger')
                continue
        x1 = []
        for i in range(num):
            while True:
                try:
                    x1.append(float(input(f'Enter number{i + 1} x1: ').strip()))
                    break
                except:
                    print(f'Should number{i + 1} x1 intiger!')
                    continue

    if x2 == None :
        while True:
            try:
                print('Should length x1 & x2 equal!')
                num = int(input('Enter Num x2: '))
                break
            except:
                print('Should Num x2 is intiger')
                continue
        x2 = []
        for i in range(num):
            while True:
                try:
                    x2.append(float(input(f'Enter number{i + 1} x2: ').strip()))
                    break
                except:
                    print(f'Should number{i + 1} x2 intiger!')
                    continue
    if len(x1) != len(x2):
        print('Should length x1 & x2 equal.')
        exit()

    if type(x1) != list and type(x2) != list:
        print('should type vectors is list!')
        exit()

    for i in range(len(x1)):
        if type(x1[i]) != int and type(x1[i]) != float:
            print('should type x1 is intiger or float!')
            exit()
    for i in range(len(x2)):
        if type(x2[i]) != int and type(x2[i]) != float:
            print('should type x2 is intiger or float!')
            exit()

    xy = []
    x22 = []
    y22 = []
    x = statistic.summ(x1)
    y = statistic.summ(x2)
    for i in range(len(x1)):
        xy.append(x1[i] * x2[i])
        x22.append(x1[i] ** 2)
        y22.append(x2[i] ** 2)

    s = (len(x1) * statistic.summ(xy)) - (x * y)
    m1 = ((len(x1) * statistic.summ(x22)) - (x ** 2)) ** 0.5
    m2 = ((len(x2) * statistic.summ(y22)) - (y ** 2)) ** 0.5

    r = s / (m1 * m2)
    
    if r > 0:
        print('X1 has a direct relationship with X2.')
        return f'pearson corr value: {r:.2f}'
    elif s < 0:
        print('X1 has an inverse relationship with X2.')
        return f'pearson corr value: {r:.2f}'
    else:
        print('X1 is not related to X2.')
        return f'pearson corr value: {r:.2f}'


def exit():
    sys.exit(0)

if __name__ == '__main__':
    main()