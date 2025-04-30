from biblioteca import estoque

nome=input("Digite o nome do produto: ")
valor=float(input("Qual é o valor do produto?: "))
quantidade=int(input("Quantos tem?: "))

print(estoque(nome, quantidade, valor))
