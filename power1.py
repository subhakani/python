def power(bas,ex):
    if(ex==1):
        return(bas)
    if(ex!=1):
        return(bas*power(bas,ex-1))
bas=int(input("Enter base: "))
ex=int(input("Enter exponential value: "))
print("Result:",power(bas,ex))
