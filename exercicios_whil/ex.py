def ex1():
    while True:
        print("Olá, Mundo")
        res=int(input('Quer continuar (Sim=1, Não =2)? '))
        if(res==2):
            break

def ex2():
    for i in range(0,110,10):
        print(i)

def ex3(num):
    for i in range(0,26):
        print(i*num)

def ex4():
    vet=[]
    for i in range(1,6):
        num=int(input(f'Digite o seu {i}º núemro: '))
        vet.append(num)
    print(f'A soma é: {sum(vet)}')

def ex5():
    maior=0
    vet=[]
    for i in range(1,6):
        num=int(input(f'Digite o seu {i}º núemro: '))
        vet.append(num)
    for i in vet:
        if(maior<i):
            maior=i
    print(f'O maior é: {maior}')

def ex6(num):
    for i in range(2,num,2):
        print(i)

def ex7(num):
    vet=[]
    while num<0:
        print('O numero é negativo!')
        num=int(input('Digite um número positivo: '))

    for i in range(1,num+1):
        vet.append(i)
    print(f'Soma dos numero: {sum(vet)}')

def ex8(num):
    vet=[]
    while num<0:
        print('O numero é negativo!')
        num=int(input('Digite um número positivo: '))

    for i in range(1,num+1):
        if(num%i==0):
            vet.append(i)
    print(vet)

def ex9():
    vet = []
    for i in range(2, 2000):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            vet.append(i)
            
    print(vet)

# ex1()
# ex2()
# ex3(3)
# ex4()
# ex5()
# ex6(35)
# ex7(10)
# ex8(28)
ex9()