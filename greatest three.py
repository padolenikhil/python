#Greatest amoung three
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if(a>b):
    if(a>c):
        print(a,"is greatest amoung three")
    else:
        print(c,"is greatest amount three")
else:
    if(b>c):
        print(b,"is Greatest amoung three")
    else:
        print(c,"is Greatest amoung three")