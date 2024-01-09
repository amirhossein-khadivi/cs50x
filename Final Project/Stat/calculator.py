# main function
def main():
    print(cmath('='))



# math function
def cmath(op= '+', x = None):
    operator = ['+', '-', '*', '/', '**', 'remainder', 'submultiple']
    while True:
        if op in operator:
            break
        else:
            print('calc Argument: ', end='')
            for i in operator:
                print(i, end=', ')
            print()
            op = input('Enter Operator: ').strip()
            

    if x == None:
        while True:
            try:
                num = int(input('Enter Num: '))
                break
            except:
                print('Should Num is intiger')
                continue
        x = []
        for i in range(num):
            while True:
                try:
                    x.append(float(input(f'Enter number{i + 1}: ').strip()))
                    break
                except:
                    print(f'Should number{i + 1} intiger!')
                    continue
    num = len(x)
    
    if op == '+':
        y = 0
        for i in range(len(x)):
            y += x[i]
        return y
    
    elif op == '-':
        for i in range(len(x)):
            if i == 0:
                y = x[i]
            else:
                y = y - x[i]
        return y 
    
    elif op == '*':
        y = 1
        for i in range(len(x)):
            y = y * x[i]

        return y
    
    elif op == '/':
        for i in range(len(x)):
            if i == 0:
                y = x[i]
            else:
                y = y / x[i]

        return y
    
    elif op == '**':
        for i in range(len(x)):
            if i == 0:
                y = x[i]
            else:
                y = y ** x[i]
        
        return y
    
    elif op == 'remainder':
        for i in range(len(x)):
            if i == 0:
                y = x[i]
            else:
                y = y % x[i]

        return y
    
    else:
        for i in range(len(x)):
            if i == 0:
                y = x[i]
            else:
                y = y // x[i]
        return y
    

if __name__ == '__main__':
    main()