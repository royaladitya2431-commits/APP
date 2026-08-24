#calculate the nth fibonacci number efficiently

#take the input from the user
n=int(input("enter the value n: "))

#If n is 0
if n==0:
    print("fibonacci number is:",0)
    
#If n is 1
elif n==1:
    print("fibonacci number is:",1)
    
#For n greater than 1
else:
    #first two fabonacci numbers
    a=0
    b=1
    
    #calculate fibonacci numbers from 2 to n
    for i in range(2, n+1):
        
        #add previous two numbers
        c=a+b
        
        #move b to a
        a=b
        
        #move c to b 
        b=c
    
    #display the nth fibonacci number
    print("fibonacci number is:",b)
