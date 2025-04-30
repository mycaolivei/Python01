def imprime_nome(nome):
    print(f"Nome:{nome}")


def solicitaNome():
    nome=input("Digite o seu nome")
    return nome

def piramide (num):
    for x in range(1, num+1,1):
        for i in range(0,x):
            print(x, end=" ")
        print()

def contaVogais(texto):
    count = 0
    for x in range(len(texto)):
        if texto[x] == "a" or texto[x] == "e" or texto[x] == "i" or texto[x] == "o" or texto[x] == "u":
            count = count + 1
    print(count)

def estoque(produto, qtd, valorUnitario):
    valortotal= qtd * valorUnitario
    return valortotal

def positivoNegativo(num):
    if num > 0:
        return "P"
    elif num == 0:
        return "Z"
    else:
        return "N"

def soma(*a):
    soma=0
    for x in range(len(a)):
        soma= soma + a[x]
    print(soma)