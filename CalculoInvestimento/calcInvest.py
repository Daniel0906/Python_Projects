
print(" 1 - CDB\n 2 - LCI\n 3 - LCA\n")

#Seleciona o investimento que o usuário escolheu
investimento  = int(input("\nSelecione o tipo de investimento: "))

#Verifica se o número digitado é válido
if investimento > 3 or investimento < 1:
    print("Código informado não consta na base, favor verificar e tentar novamente!")

else:

    #Atribui o nome do investimento ao número dele na variável
    if investimento == 1:
        investimento = "CDB"

    elif investimento == 2:
        investimento = "LCI"

    elif investimento == 3:
        investimento = "LCI"

    #Recebe o valor que o cliente quer resgatar e transforma no tipo float 
    vlResgatado   = input("Digite o valor a ser resgatado: ")
    vlResgatado = float(vlResgatado)

    #Recebe a quantidade de dias investidos e transforma em inteiro
    diasInvestido = int(input("Digite o número de dias investido: "))

    #Condição para filtrar a quantidade de dias
    if diasInvestido <= 180:

        #Cálculo do valor do imposto com base no valor resgatado
        imposto = vlResgatado * (22.5 / 100)
        print("\n Tipo de Investimento: {} \n Valor Resgatado: R${:.2f} \n Dias Investido: {} dias \n Alíquota do IR: 22.5% \n Valor do Imposto: R${:.2f}".format(investimento, vlResgatado, diasInvestido, imposto))

    elif diasInvestido > 180 and diasInvestido <= 360:
        imposto = vlResgatado * (20 / 100)
        print("Tipo de Investimento: {} \n Valor Resgatado: R${:.2f} \n Dias Investido: {} dias \n Alíquota do IR: 20% \n Valor do Imposto: R${:.2f}".format(investimento, vlResgatado, diasInvestido, imposto))

    elif diasInvestido > 361 and diasInvestido <= 720:
        imposto = vlResgatado * (17.5 / 100)
        print("Tipo de Investimento: {} \n Valor Resgatado: R${:.2f} \n Dias Investido: {} dias \n Alíquota do IR: 17.5% \n Valor do Imposto: R${:.2f}".format(investimento, vlResgatado, diasInvestido, imposto))

    elif diasInvestido > 720:
        imposto = vlResgatado * (15 / 100)
        print("Tipo de Investimento: {} \n Valor Resgatado: R${:.2f} \n Dias Investido: {} dias \n Alíquota do IR: 15% \n Valor do Imposto: R${:.2f}".format(investimento, vlResgatado, diasInvestido, imposto))

        