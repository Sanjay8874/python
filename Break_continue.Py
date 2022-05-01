#Break and continue statements..
#prints value from 1 to 45
"""i = 0
while(True):
    i = i+1
    print(i)
    if i == 45:
        break
    
"""

#print value from 5 to 50

i = 0  # initia value of i = 0
 
while(True): #While true represent value always True 
    if i+1<5:
        i = i+1
        continue
    
    print(i+1)
    if i == 44:
        break
    i = i+1
    
    
# Take input from user until exceed 100   

while(True):
    j = int(input("Enter values"))
    if j<=100: 
        print("Success")
        continue
    if j>100:
        print("unsuccess")
        break
        