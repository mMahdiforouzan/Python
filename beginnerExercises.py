#Given two integer numbers,
#write a Python program to return their product only if the product is equal to or lower than 1000. 
#Otherwise, return their sum.

def exercise1(x,y):
    if(x*y<1000):
        return x*y
    else:
        return x+y
    

