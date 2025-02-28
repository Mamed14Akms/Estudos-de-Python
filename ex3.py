print("Irei calcular a área de qualquer círculo para você")

raio = float ( input("Informe o raio do circulo: "))
medida = int (input("Escolha em que medida eu devo usar: km: 1, m: 2, cm: 3 e mm: 4  :"))
print("OBS: Usaremos 3,14 como valor de π")

area = 3.14 * raio ** 2

if medida <= 1:
    print("A área do circulo será: ", area, "km" )

elif medida <= 2:
    print("A área do circulo será: ", area, "m" )

elif medida <= 3:
    print("A área do circulo será: ", area, "cm" )

else:
    print("A área do circulo será: ", area, "mm" )