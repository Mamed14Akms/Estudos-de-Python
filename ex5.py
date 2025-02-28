print("Irei calcular a área de qualquer retângulo para você")

l = float ( input("Informe o tamanho da lateral do retângulo: "))
b = float (input ("Informe o tamanho da base do retângulo: "))

medida = int (input("Escolha em que medida eu devo usar: km: 1, m: 2, cm: 3 e mm: 4  :"))

area = l * b 

if medida <= 1:
    print("A área do retângulo será: ", area, "km" )

elif medida <= 2:
    print("A área do retângulo será: ", area, "m" )

elif medida <= 3:
    print("A área do retângulo será: ", area, "cm" )

else:
    print("A área do retângulo será: ", area, "mm" )