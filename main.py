import beginnerExercises as beginnerExercises
import randomDataGen as dataGen
import random as random

print("select which exercise")
inputValue = int(input())

match inputValue: 
     case 1:
          for counter in range(10):
            x = random.randint(0,50)
            y = random.randint(0,50)
            z = beginnerExercises.exercise1(x,y)         
            print("x   y   sum product answer")
            print("%d  %d  %d    %d      %d"%(x,y,x+y,x*y,z))
     case 2:
        beginnerExercises.exercise2()

     case 3:
        print("give a string!")
        stringValue = input()
        beginnerExercises.exercise3(stringValue)

     case 4:
        print("give a string!")
        word = input()
        print("give a number!")
        n = int(input())
        print(beginnerExercises.exercise4(word,n))

     case 5 | 6:
        counter = 0
        thisList = []
        thisList.append(int(input()))
        while(thisList[len(thisList)-1]>=0):
               thisList.append(int(input()))
     
        thisList.pop(len(thisList)-1)
        if inputValue == 5:
          print(beginnerExercises.exercise5(thisList))
        if inputValue == 6:
            beginnerExercises.exercise6(thisList)

     case 7:
        print("enter min")
        min = int(input())
        print("enter max")
        max = int(input())
        print("enter how many random numbers you want")
        n = int(input())
        print("enter what you want all the numbers to be divisible by")
        delta = int(input())
        print(dataGen.randomIntN(min,max,n,delta))

     case 8:
        x = dataGen.lottery(100,10)
        print(x)
        print(random.sample(x,2))
