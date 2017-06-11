import os
import sys
import math


decimals = [128,64,32,16,8,4,2,1]

start = [0,0,0,0,0,0,0,0]

print("Enter a binary number")
binary = sys.stdin.readline()

result=[]

for i in range(8):
    start[i] = binary[i]
    if(start[i]=="1"):
        result.append(decimals[i])

print(sum(result))    
    



number = int(input('Enter a decimal number '))

number

temp = []


while (number >=1):
    
    if(number%2 != 0):
        number = number/2
        number = math.floor(number)
        
        temp.append(1)
    else:
        number = number/2
        
        temp.append(0)

while(len(temp) < 8):
    if(number%2 != 0):
       number = number/2
       number = math.floor(number)
        
       temp.append(1)
    else:
       number = number/2
        
       temp.append(0)


        
final = list(reversed(temp))
print(final)
    
    
    

