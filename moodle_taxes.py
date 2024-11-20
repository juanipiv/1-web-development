ingresos = int(input("¿cuales son sus ingresos?:"))
limit_1=12450
limit_2=20000
limit_3=35000
limit_4=60000
limit_5=300000

if ingresos < limit_1:
    print ('su IRPF es del 19%, va a tener que pagar' ingresos*0.19 'de impuestos, por lo que le llegarian' ingresos - ingresos*0.19 'de forma neta'
          
if  limit_1 <= ingresos < limit_2
    print ("su IRPF es del 24%, va a tener que pagar" ingresos*0.24 "de impuestos, por lo que le llegarian" ingresos - ingresos*0.24 "de forma neta"

if  limit_2 <= ingresos < limit_3 :
    print ("su IRPF es del 30%, va a tener que pagar" ingresos*0.30 "de impuestos, por lo que le llegarian" ingresos - ingresos*0.30 "de forma neta"

if  limit_3 <= ingresos < limit_4 :
    print ("su IRPF es del 37%, va a tener que pagar" ingresos*0.37 "de impuestos, por lo que le llegarian" ingresos - ingresos*0.37 "de forma neta"

if  limit_4 <= ingresos < limit_5 :
    print ("su IRPF es del 45%, va a tener que pagar" ingresos*0.45 "de impuestos, por lo que le llegarian" ingresos - ingresos*0.45 "de forma neta"
          
if  limit_5 <= ingresos :
    print ("su IRPF es del 47%, va a tener que pagar" ingresos*0.47 "de impuestos, por lo que le llegarian" ingresos - ingresos*0.47 "de forma neta"
