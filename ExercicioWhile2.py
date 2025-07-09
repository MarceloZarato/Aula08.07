#Mostrar um menu até a pessoa digitar "Sair"

menu = input ("Digite sair:")

while menu != "sair":
    print ("Opção errada")
    menu = input ( "Digite Novamente:")
print ("Saiu")