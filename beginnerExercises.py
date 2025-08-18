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
        print("Current number: %d Previous number: %d sum: %d"%(x,x0,x+x0))
        x0=x
        x=x+1
    return


#Write a Python code to accept a string from the user and display characters present at an even index number.
def exercise3(stringValue):
    for x in range(0,len(stringValue),2):
        print(stringValue[x])


#Write a Python code to remove characters from a string from 0 to n and return a new string.
def exercise4(word,n):
    return word[n:]

#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
def exercise5(thisList):
    return thisList[0]==thisList[len(thisList)-1]

#Write a Python code to display numbers from a list divisible by 5
def exercise6(thisList):
    for x in range(len(thisList)-1):
        if((thisList[x]%5)==0):
            print(thisList[x])