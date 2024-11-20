a = int(input("please enter the fist number:"))
b = int(input("please enter the second number:"))

result = 1
limit = min(a,b)

for i in range(2, limit + 1):
    if a % limit == 0 and b % limit == 0:
        result = i
print("the greatest common divisor is: ", result)
