def to_binary(n):
    if n == 0:
        return '0'
    output = ''
    while n >= 1:
        output = str(n % 2) + output
        n = n // 2
    return output

input = int(input("\nPlease input the base 10 number to be converted: "))

print(f'\n{input} in binary: {to_binary(input)}\n')