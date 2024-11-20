# calcular el numero en binario

number = int(input("enter your number:"))
result = ""

while number > 1:
    remainder = number % 2
    number = int (number / 2)
    result = str(remainder) + result
result = "1" + result # es necesario por que como se empieza en el ultimo consciente, este siempre sera 1
print (result, "as binary")
