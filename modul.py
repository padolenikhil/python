import lcm1

#For LCM

num1 = int(input("Enter first number for LCM: "))  
num2 = int(input("Enter second number for LCM: "))  
print("The L.C.M. of", num1,"and", num2,"is", lcm1.calculate_lcm(num1, num2)) 

#For GCD
i=int(input("Enter no. for GCD i :"))
j=int(input("Enter no. for GCD j :"))
print("The gcd of no. is :", lcm1.gcd(i,j))

#For co prime numbers
print(lcm1.are_coprime2)