import math

def Ex1(raio: float):
    """
        Calcule a área de um círculo com raio 5. Use a fórmula: área = π * raio^2. (Dica: você pode usar 3.14159
        como valor aproximado de π).
    """
    area = math.pi * raio ** 2

    print(f"A area do circulo é {area}")

def Ex2(Fahrenheit: float):
    """
        Converta uma temperatura de Fahrenheit para Celsius. A fórmula de conversão é:
        Celsius = (Fahrenheit - 32) * 5/9
    """
    Celsius = (Fahrenheit-32)* 5/9

    print(f"A temperatura de Fahrenheit para Celsius é {Celsius}")

def Ex4(qtd_livro: int, qtd_caneta: int):
    """
        Você comprou 3 livros por R$ 25 cada e 2 canetas por R$ 5 cada. Calcule o total gasto.
    """
    gasto=(qtd_livro*25)+(qtd_caneta*5)

    print(f"Você gastou: R${gasto}")

def Ex5():
    """
        Um carro percorreu 150 km a uma velocidade média de 60 km/h. Quanto tempo (em horas) o carro
        levou para percorrer essa distância?
    """
    distancia=150/60

    print(f"Para percorrer essa distância ele demorou {distancia} horas")

def Ex6(A,B):
    """
        Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
        aritmética do aluno.
    """
    media=(A+B)/2

    print(f"A média aritmética do aluno é {media}")

def Ex7(A: float,B: float):
    """
        Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
        ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.
        ▪ Exemplo: nota a * 4 e nota b * 6
    """
    media=(A*0.4+B*0.6)

    print(f"A média ponderada do aluno é {media}")

def Ex8(peca1_valor: float,peca2_valor: float):
    """
        Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que
        o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor
        unitário de cada peça2. Após, calcule e mostre o valor a ser pago.
    """
    valor=peca1_valor+peca2_valor

    print(f"O valor a ser pago é {valor}")

def Ex9(valor_produto: float,valor_pago: float):
    """
        Crie um programa que receba o valor do produto e valor pago.
        Calcule o troco a ser pago.
        O valor do troco deve ser exibido no terminal
    """
    valor=valor_pago-valor_produto

    print(f"Seu troco é R${valor}")



Ex1(2)
Ex2(32)
Ex4(1,1)
Ex5()
Ex6(2,2)
Ex7(10,10)
Ex8(10,10)
Ex9(10,20)