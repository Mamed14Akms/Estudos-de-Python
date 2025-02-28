print("irei calcular os juros de deposito bancario")

valor = float (input("O valor do depositado: R$"))
anos = int (input("De quantos anos foi o deposito: "))
taxa = int (input ("De quanto foi a taxa: "))

taxa = taxa/100

juros = valor*anos*taxa

montante = valor + juros

print("O juros do seu deposito bancario foi de: R$", montante )