#Atribuindo o valor da dívida a variável
vlDivida = input("Digite o valor da dívida:\n")

#Transformando o valor em float
vlDivida = float(vlDivida)

#Valor fixo sem acréscimo
print("Total:R${:.2f} Juros: R$0,00 Número de parcelas: 1 Valor da Parcela: R${:.2f}".format(vlDivida, vlDivida))

#Criação da variável para o acréscimo de juros
juros = 5

#For para um range de 3 a 12 parcelas, contando de 3 em 3
for x in range(3,15,3):

    #Acréscimo de juros para cada ciclo do for
    juros = juros + 5

    #Valor total da dívida com o acréscimo de juros
    total = vlDivida + (vlDivida*(juros/100))

    #Valor do juros acrescentado 
    vlJuros = vlDivida*(juros/100)

    #Valor da parcela para cada parcelamento
    vlParcela = total/x
    print("Total:R${:.2f} Juros: R${:.2f} Número de parcelas: {} Valor da Parcela: R${:.2f}".format(total, vlJuros, x, vlParcela))
    
