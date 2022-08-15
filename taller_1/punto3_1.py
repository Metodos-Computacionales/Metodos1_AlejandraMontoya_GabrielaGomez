

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res*int(i)
    print (res)
    return res



#Sin input 
def factorial_20():
    lst =[]
    for j in range (1,20):
        res = 1
    for i in range(1,j):
        res = res*int(i)
        lst.append(res)
    print ("Los primeros 20 numeros factoriales son: {todos} ".format(todos=lst))
    return lst




    