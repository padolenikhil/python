#program for check if a number is prime or not

a=int(input("Enter any number:"))

if(a==1):
    print(a,"is not a prime number")
elif(a>1):
    for i in range(2,a):
        if(a % i)==0:
            print(a,"is not a prime number")
            break
        else:
            print(a,"is a prime number")
else:
    print(a,"is not a prime number")