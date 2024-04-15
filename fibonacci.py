#Program to display the Fibonacci sequence up to n-th term
n=int(input("How many terms:"))
a,b=0,1
count=0
if(n<=0):
    print("please enter a positive numbers")
elif(n==1):
    print(a)
else:
    print("Fibonacci sequence:")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1