#Criação das váriaveis para o contador
seg = 0
ter = 0
qua = 0
qui = 0
sex = 0

#Seletor de Opções
print("\nSelecione um dia da semana:\n") 
print(" 1 - Segunda-feira\n 2 - Terça-feira\n 3 - Quarta-feira\n 4 - Quinta-feira\n 5 - Sexta-feira\n")

#For para um range de 10 funcionários
for x in range(10):

    #Variavel auxiliar para receber o codigo do cliente
    aux = int(input("Selecione um Número: "))
    
    #Estrutura if para armazenar os votos
    if (aux == 1):
        seg = seg + 1
    elif (aux == 2):
        ter = ter + 1
    elif (aux == 3):
        qua = qua + 1
    elif (aux == 4):
        qui = qui + 1
    elif (aux == 5):
        sex = sex + 1 
    else: 
        #Retorno caso seja digitado algo diferente das opções
        print("Opção inválida!")

#Resultado dos votos
print("\nResultado da votação:\n")
print("Segunda-feira: {}\n".format(seg))
print("Terça-feira: {}\n".format(ter))
print("Quarta-feira: {}\n".format(qua))
print("Quinta-feira: {}\n".format(qui))
print("Sexta-feira: {}\n".format(sex))

#Estrutura if para verificar qual dia da semana foi escolhido
if (seg > ter and seg > qua and seg > qui and seg > sex):
    print("Segunda-feira ganhou a votação!\n")
elif (ter > seg and ter > qua and ter > qui and ter > sex):
    print("Terça-feira ganhou a votação!\n")
elif (qua > seg and qua > ter and qua > qui and qua > sex):
     print("Quarta-feira ganhou a votação!\n")
elif (qui > seg and qui > ter and qui > qua and qui > sex):
     print("Quinta-feira ganhou a votação!\n")
else:
     print("Sexta-feira ganhou a votação!\n")