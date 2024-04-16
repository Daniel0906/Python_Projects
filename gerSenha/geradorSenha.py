import random

def passw_generator():
    get_length_pass = int(input("Digite a quantidade de caracteres desejados: \n"))
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers    = "1234567890"
    spc_carac  = "!@#$%¨&*"

    join_carac = lower_case + upper_case + numbers + spc_carac

    passw = "".join(random.sample(join_carac, get_length_pass))

    print("-" * 20)
    print("Senha Gerada: " + passw)
    print("-" * 20)

while True:
    passw_generator()
    new_passw = int(input("Deseja gerar uma nova senha? 1 - Sim / 2 - Não: "))

    if new_passw != 1:
        break

print("Finalizando gerador...")