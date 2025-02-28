print("irei calcular os juros de deposito bancario")

valor = float (input("O valor do depositado: R$"))
meses = int (input("De quantos meses foi o deposito: "))
taxa = int (input ("De quanto foi a taxa: "))
opcao = int (input("Caso você deseje adicionar o valor de entrada, digite 1, caso não queira digite 2: "))


if opcao <= 1:
    entrada = float (input("Qual é o valor de entraada: R$"))

    valor = valor - entrada    
    taxa = taxa/100

    juros = valor*meses*taxa

    montante = valor + juros

    print("O juros do seu deposito bancario foi de: R$", montante )

else:  
    taxa = taxa/100

    juros = valor*meses*taxa

    montante = valor + juros

    print("O juros do seu deposito bancario foi de: R$", montante )