from datetime import date
from pygame import mixer

def ex1():
    mixer.init()
    mixer.music.load('audio_ramdom.mp3')
    mixer.music.play()
    print('Que musicona!!!')


def ex2(num:float):
    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")

def ex3(num:float, num1:float):
    if num>num1:
        print(f"{num} é maior que {num1}.")
    elif num==num1:
        print(f"{num} é igual a {num1}.")
    else:
        print(f"{num} é menor que {num1}.")

def ex4(num:float, num1:float, num2:float, num3:float):
    media=(num+num1+num2+num3)/4
    if media>=7:
        print("Aprovado")
    elif media>=5:
        print("Em recuperação")
    else:
        print("Reprovado")

def ex5(num:float, num1:float):
    if(num>num1):
        if num % num1 == 0:
            print(f"{num} e {num1} são múltiplos entre si.")
        else:
            print(f"{num} e {num1} não são múltiplos entre si.")
    else:
        if num1 % num == 0:
            print(f"{num} e {num1} são múltiplos entre si.")
        else:
            print(f"{num} e {num1} não são múltiplos entre si.")

def ex6(num:float, num1:float, operacao:chr):
    if operacao=='+':
        print(num+num1)
    elif operacao=='-':
        print(num-num1)
    elif operacao=='*':
        print(num*num1)
    elif operacao=='/':
        print(num/num1)
    else:
        print('use essas operações matemáticas (+, -, *, /)!!!')

def ex7(ano:int):
    idade=int(date.today().year-ano)
    if idade>=18:
        print("o voto é obrigatório este ano")
    elif idade>=16:
        print("o voto é opcional este ano")
    else:
        print("o voto é proibido este ano")

def ex8(salario_atual:float):
    if salario_atual <= 280:
        percentual = 20
    elif salario_atual <= 700:
        percentual = 15
    elif salario_atual <= 1500:
        percentual = 10
    else:
        percentual = 5

    valor_aumento = salario_atual * (percentual / 100)
    novo_salario = salario_atual + valor_aumento

    print(f"\nSalário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: R$ {valor_aumento:.2f}")
    print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")

def ex9(cod_estado:int,peso_ton:float,cod_carga:int):
    peso_quilos = peso_ton * 1000

    if 10 <= cod_carga <= 20:
        preco_por_quilo = 100
    elif 21 <= cod_carga <= 30:
        preco_por_quilo = 250
    else: # 31 a 40
        preco_por_quilo = 340

    preco_carga = peso_quilos * preco_por_quilo

    if cod_estado == 1:
        porcentagem_imposto = 0.35
    elif cod_estado == 2:
        porcentagem_imposto = 0.25
    elif cod_estado == 3:
        porcentagem_imposto = 0.15
    elif cod_estado == 4:
        porcentagem_imposto = 0.05
    else:
        porcentagem_imposto = 0.0

    valor_imposto = preco_carga * porcentagem_imposto

    valor_total = preco_carga + valor_imposto

    print(f"\n--- Resumo do Transporte ---")
    print(f"Peso convertido: {peso_quilos:.2f} kg")
    print(f"Preço da carga: R$ {preco_carga:.2f}")
    print(f"Valor do imposto: R$ {valor_imposto:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")

def ex10(A:int,B:int,C:int):
    if A>=B+C:
        print("NAO FORMA TRIANGULO")
    if A**2==B**2+C**2:
        print("TRIANGULO RETANGULO")
    if A**2>B**2+C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2<B**2+C**2:
        print("TRIANGULO ACUTANGULO")
    if A**2<B**2+C**2:
        print("TRIANGULO ACUTANGULO")
    if A==B==C:
        print("TRIANGULO EQUILATERO")
    if A==B or B==C or A==C:
        print("TTRIANGULO ISOSCELES")

# ex1()

ex2(4)

ex3(3,2)

ex4(6,6,7,9)

ex5(2,4)

ex6(1,2,'*')

ex7(2008)

ex8(100000)

ex9(1,5,10)

ex10(1,3,3)