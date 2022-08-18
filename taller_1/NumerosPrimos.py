
def primos():
    total=0
    lst = []
    n = 16
    while total < 10:
        for i in range(2,n-1):
            if (n%i == 0):
                n +=1
            else:
                lst.append(n)
                total += 1
                n+=1
    print(lst)
    return lst
        
primos()

