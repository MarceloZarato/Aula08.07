cliente={"nome": "Pascoal", "numero": 11954632223, "idade": 25, "CPF": "12345678977", "Endereço":"Rua Tito"}
print (cliente)
print (len(cliente))
print(cliente["Endereço"])
del (cliente["nome"])
print(cliente)
print(len(cliente))
cliente["nome"] = "Marcelo"
print(cliente)
print(len(cliente))