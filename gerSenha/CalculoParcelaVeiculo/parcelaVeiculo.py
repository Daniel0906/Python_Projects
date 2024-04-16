#Atribuindo o preço do carro a variável
valor = input("Digite o preço do carro: ")

#Transformando a variável em float
valor = float (valor)

#Criação do cálculo utilizado para determinar o desconto da compra á vista
desc = valor - (valor*0.20)
print("Preço final á vista com desconto de 20%: {:.2f} " .format(desc))

#Criação da variável para o acréscimo de juros
juros = 0

#For para um range de 6 a 60 parcelas, contando de 6 em 6
for x in range(6,66,6):

    #Acréscimo do juros para cada ciclo do for
    juros  = juros + 3

    #Acréscimo do valor somado ao juros
    acresc  = valor + (valor*(juros/100))

    #Valor da parcela para cada parcelamento
    parcela = acresc / x
    print("Preço final parcelado em {}x é de: R${:.2f} com parcelas de: R${:.2f}".format(x, acresc, parcela))