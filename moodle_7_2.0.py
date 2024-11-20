a = int(input("please enter the fist number:"))
b = int(input("please enter the second number:"))

result = 1
limit = min(a,b)

for i in range(limit, 1, - 1):
    if a % limit == 0 and b % limit == 0:
        result = i
        break
print("the greatest common divisor is: ", result)
