a = int(input("please enter the first number: "))
b = int(input("please enter the first number: "))

m = max(a, b)
n = min(a, b)

while n > 0:
    remainder = m % n
    if remainder == 0:
        result = n
        break
    m = n
    n = remainder

print("the greatest common divisor is: ", result)
