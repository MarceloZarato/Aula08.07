#Desafio Final For + Lista + entrada

#pedir o nome de 3 pessoas
#guardar o nome em uma lista
#dar boas vindas a cada uma


nomes = []

for i in range(3):
    nomes.append(input("Digite um nome:"))
    
for i in nomes:
    print(f"Boas Vindas {i}")
print("Fim")
