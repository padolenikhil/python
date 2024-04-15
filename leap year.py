#program for check entered year is leap or not
n=int(input("Enter a year:"))
if(n%100==0 and n%400==0):
    print(n,"is a century leap year")

elif(n%100!=0 and n%4==0):

    print(n,"is a leap year")

else:
    print(n,"is not a leap year")