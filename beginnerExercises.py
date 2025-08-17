#Given two integer numbers,
#write a Python program to return their product only if the product is equal to or lower than 1000. 
#Otherwise, return their sum.

def exercise1(x,y):
    if(x*y<1000):
        return x*y
    else:
        return x+y

#Write Python code to iterate through the first 10 numbers and,
#in each iteration, print the sum of the current and previous number 
def exercise2():
    sum=0
    x=0
    x0=0
    for x in range(10):
        print("Current number: %d Previous number: %d sum: %d"%(x0,x,x+x0))
        x=x+1
        x0=x0+1