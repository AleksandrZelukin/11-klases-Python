def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary = ""
    num = abs(decimal_num)
    
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    
    if decimal_num < 0:
        binary = "-" + binary
        
    return binary

# Example usage
number = int(input("Enter a decimal number: "))
result = decimal_to_binary(number)
print(f"The binary representation of {number} is: {result}")