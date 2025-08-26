import random, secrets, string
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
    
    i=0
    while(numberOfTickets>len(lotterySet) and len(lotterySet)<(numbersInRange) and i<100):
        numbers = random.sample(range(min,max),numberOfTickets-len(lotterySet))
        for x in range(len(numbers)-1):
            lotterySet.add(numbers[x])
    print (numbersInRange,len(lotterySet))
    return [*lotterySet]


#generate 6 digit random secure OTP
def OneTimePassword():
    password = ''.join(secrets.choice(string.digits) for i in range(6))
    return password
    
#pick a random character from a string
def randomChar(str):
    return random.choice(str)

#Write a code to generate random string of length 5.
# Note: String must be the combination of the UPPER case and lower case letters only.
#       No numbers and a special symbol.
def randomString(n):
    str = ''.join(secrets.choice(string.ascii_letters) for i in range(n))
    return str

# Write a code to generate a random password which meets the following conditions.
#     Password length must be 10 characters long.
#     It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
