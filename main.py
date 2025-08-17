import beginnerExercises as beginnerExercises
import random as random

print("select which exercise")
input = input()

#match input: 
#   case 1:
for counter in range(10):
    x = random.randint(0,50)
    y = random.randint(0,50)
    z = beginnerExercises.exercise1(x,y)         
    print("x   y   sum product answer")
    print("%d  %d  %d    %d      %d"%(x,y,x+y,x*y,z))
  #  case 2:
beginnerExercises.exercise2()
    