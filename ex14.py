ano = int(input("Informe o ano que você deseja: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print ("O ano de ", ano, "é um ano bissexto.")
else:
    print ("O ano de ", ano, "não é um ano bissexto.")