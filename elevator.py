import time

def exponentiallgrowthbyone(product,exponent):
    x = product
    n = exponent
    while(True):

        x=x+1
        n=n+1
        print(str(x**n) + "\n")
