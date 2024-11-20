# calcular todos los divisores de un numero dado

number = int(input("enter your number:"))

for i in range(1,number + 1):
    remainder = number % i
    if remainder == 0:
        print (i)

# mas eficiente

print(1)
for i in range(2,number//2 + 1):
    remainder = number % i
    if remainder == 0:
        print (i)
print(number)
