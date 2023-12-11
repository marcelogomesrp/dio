
limit = 500
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """

[d] Depositoar
[s] Sacar
[e] Extrato
[q] Sair


"""



def depositar() -> None:
    global saldo
    global extrato
    print("*** Depositar ***")
    valor = 0
    while(valor <= 0):
        try:    
            valor = float(input("Entre com o valor: "))
            if valor <=0:
                print("O valor informado deve ser um número maior que zero.")
        except:
            print("O valor informado deve ser um número maior que zero.")
    saldo+= valor
    extrato+=f"Deposito: R$ {valor:.2f}\n"
    print(f'Deposito realizado com sucesso no valor de {valor:.2f}.')    
    pass

def sacar() -> None:
    global saldo
    global extrato
    global numero_saques
    valor = 0
    print("*** Sacar ***")
    if numero_saques >= LIMITE_SAQUES:
        print("Antigido o limite máximo de saques.")
        return
    
    while(valor <= 0 or valor > 500):
        try:    
            valor = float(input("Entre com o valor: "))
            if valor <=0 or valor > 500:
                print("O valor informado deve ser um número maior que zero e menor que 500.")
        except:
            print("O valor informado deve ser um número maior que zero e menor que 500.")

    if valor <= saldo:
        numero_saques+=1
        saldo-=valor
        extrato+=f"Saque: R$ {valor:.2f}\n"
        print("Saque efetuado com sucesso")
    else:
        print("Sem saldo suficiente para concluir esta operacao")



def ver_extrato() -> None:
    print("*** Extrato ****")
    print(extrato)
    print(f"Saldo: {saldo}")

def main() -> None:
    op = ''
    while op != "q":
        op = input(menu).strip().lower()
        
        match op:
            case "d":
                depositar()
            case "s":
                sacar()
            case "e":
                ver_extrato()
            case "q":
                print("bye")
            case _:
                print("Opção invalida")
        
    

if __name__ == '__main__':
    main()
