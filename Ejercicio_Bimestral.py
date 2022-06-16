print("-----------------------------")
print("-------Canjear Cheques-------")
print("-----------------------------")

#input
Valor_cheque=int(input("ingrese el valor de su cheque: "))
if Valor_cheque%100==0:
    pass
else:
    print("el valor de su cheque debe ser un multiplo de 100")

#determino unas variables que voy a necesitar
Total_dinero=0
número_transaccion=0
billetes_de_10000=0
billetes_de_2000=0
monedas_de_100=0
contador_10000=0
contador_2000=0
contador_100=0

#Procesing

while Valor_cheque!=0:
    if Valor_cheque%100==0:
        Valor_cheque//10000
        billetes_de_10000 = Valor_cheque//10000
        billetes_de_2000 = (Valor_cheque%10000)//2000
        monedas_de_100 = ((Valor_cheque%10000)%2000)//100

        print("el cajero debe entregar:")
        print(billetes_de_10000,"billetes de 10000")
        print(billetes_de_2000,"billetes de 2000")
        print(monedas_de_100,"monedas de 100")

        contador_10000= contador_10000+billetes_de_10000
        contador_2000= contador_2000 + billetes_de_2000
        contador_100= contador_100 + monedas_de_100
        Total_dinero=Total_dinero+Valor_cheque
        número_transaccion=número_transaccion+1
    else:
        print("el valor de su cheque debe ser un multiplo de 100")
    

    Valor_cheque=int(input("ingrese el valor de su cheque: "))
    
#output

print("Es cierre de día.")
print("Hoy se entregaron: ") 
print("Billetes de 10000: ",contador_10000)
print("Billetes de 2000: ",contador_2000)
print("Monedas de 100: ",contador_100)
print("En total hoy se entregó: ",Total_dinero)
print("En un total de ", número_transaccion," transacciones")
