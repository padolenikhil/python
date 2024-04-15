#convert decimal to binary
def dec_to_binary(n):
    return bin(n).replace("0b", "")

# convert decimal to octal
def dec_to_octal(n):
    return oct(n).replace("00", "")

# convert decimal to hexadecimal
def dec_to_hexadecimal(n): 
    return hex(n).replace("0x", "")

#user input
num = int(input("Enter a decimal number: "))
print(f"Binary: {dec_to_binary(num)}")
print(f"octal: {dec_to_octal(num)}")
print(f"Hexadecimal: {dec_to_hexadecimal(num)}")