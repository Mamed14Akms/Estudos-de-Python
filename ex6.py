valor_uni = float (input ("Me informe o valor unitário da sua mercadoria: "))
quantidade = int (input ("Me informe a quantidade dos itens: "))

total_i = valor_uni * quantidade

Pagamento =  float (input ("Informe o valor que você irá pagar: "))

total = Pagamento - total_i

if total <= 0:

    print("A compra de ", quantidade, "do protudo foi de R$", total_i, "Obrigado por comprar conosco!!!")

else:
    print("A compra de ", quantidade, "unidades do protudo foi de R$",total_i, ".O seu troco foi de R$ ", total, "Obrigado por comprar conosco!!!")