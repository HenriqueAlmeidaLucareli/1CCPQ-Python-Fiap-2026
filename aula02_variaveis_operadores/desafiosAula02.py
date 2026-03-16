def Desafio01():
    nome=str(input("Digite o seu nome: "))
    return print(f"Bem vindo {nome}!")

def Desafio02():
    dia_nascimento=str(input("Digite o dia do seu nascimento: "))
    mes_nascimento = str(input("Digite o mes do seu nascimento: "))
    ano_nascimento = str(input("Digite ao ano do seu nascimento: "))

    return print(f"Essa é a sua data de nascimento: {dia_nascimento}/{mes_nascimento}/{ano_nascimento}!")

def Desafio03():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))

    return print(f"A soma de {num1} + {num2} é igual a {num1+num2}!")

Desafio01()
Desafio02()
Desafio03()