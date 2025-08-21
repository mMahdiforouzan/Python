import random,secrets
#Write a code to generate 3 random integers between 100 and 999 which is divisible by 5
def randomIntN(min,max,n,delta):
    numbers=[random.randrange(min,max,delta)]
    
    for x in range(n-1):
        numbers.append(random.randrange(min,max,delta))

    return numbers




#Write a code to generate 100 random lottery tickets
 #conditions:
   # The lottery number must be 10 digits long.
   # All 100 ticket number must be unique.

def lottery(numberOfTickets,digitLength):
    min=pow(10,digitLength-1)
    max=pow(10,digitLength)-1
    numbersInRange = max-min
    init = random.sample(range(min,max),numberOfTickets)
    lotterySet = {*init}
    print (numbersInRange,len(lotterySet))

    while(numberOfTickets>len(lotterySet) and len(lotterySet)<(numbersInRange) and i<100):
        numbers = random.sample(range(min,max),numberOfTickets-len(lotterySet))
        for x in range(len(numbers)-1):
            lotterySet.add(numbers[x])
    print (numbersInRange,len(lotterySet))
    return [*lotterySet]
