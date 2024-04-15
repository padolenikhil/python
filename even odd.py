#program to check  Enter no. is Even or odd
a=int(input("Enter a Number:"))
if(a%2==0):
    print(a,"is an even number")
else:
    print(a,"is an odd number")
# program for Greatest amoung two
a=int(input("Enter the first number:"))
b=int(input("Enter the second Number"))
if(a>b):
    print(a,"is Greatest amoung two")
else:
    print(b,"is Greatest amoung two")

#Program to swapping two numbers
    a=int(input("Enter the 'a' value:"))
    b=int(input("Enter the 'b' value"))
    c=a
    a=b
    b=c
    print("The value for a is",a)
    print("The value for a is",b)