# main function
def main():
    print(s())

# sterling number function
def s():
    while True:
        try:
            n = int(input('Enter n: ').strip())
            break
        except:
            print('Should n intiger!')
            continue
    while True:
        try:
            k = int(input('Enter k: ').strip())
            break
        except:
            print('Should k intiger!')

    kfact = 1
    for i in range(1, k + 1):
        kfact = i * kfact
    

    summation = []
    for i in range(k + 1):
        ifact = 1
        for j in range(1, i + 1):
            ifact = j * ifact
        
        kifact = 1
        for j in range(1, (k - i) + 1):
            kifact = j * kifact
        
        # Composition
        c = kfact / (ifact * kifact)

        # prod
        p = ((-1) ** i) * c * ((k - i) ** n)
        
        summation.append(p)
    
    # Summation
    Sum =sum(summation)

    return Sum / kfact




if __name__ == '__main__':
    main()