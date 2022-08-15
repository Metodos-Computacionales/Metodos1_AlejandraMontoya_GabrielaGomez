import punto3_1 as fac 


def variations():
    n = int(input("Provide a number of elements: "))
    r = int(input("Provide a number of variations: "))
    res = fac.factorial(n)/(fac.factorial((n-r)))
    print(res)
    pass
#variations

def combination():
    n = int(input("Provide a number of elements: "))
    m = int(input("Provide a number of possible groups: "))
    if n<m:
        print("El numero de elementros n debe ser mayor a m")
        pass
    else: 
        res = fac.factorial(n)/(fac.factorial(m)*(fac.factorial((n-m))))
        print("El numero de combinaciones es", res)
        return res
combination()
