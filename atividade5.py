#Vá em uma loja online de computadores, faça uma lista de itens para montar um pc gamer.
#Não esqueça de colocar um gabinetecooler master e uma placa de vídeoGeForce RTX 2080Ti.
#A.Depois de ir para o carrinho de compras na loja online, 
# você percebeu que o gabinete cooler master e a placa GeForce RTX 2080Tipassaram do valor do seu orçamento 
# para montar seu pc gamer. Então REMOVA os dois itens da sua lista.

listaPC = ["Gabinete Cooler Master", "Placa de Vídeo GeForce RTX 2080Ti"]
somaLista = 0

listaPC[0] = (500)
listaPC[1] = (900)

for soma in listaPC:
    somaLista += soma

print("Preço dos produtos: ",somaLista)

valor   = (int(input("Insira aqui o valor do seu orçamento: ")))

print("Analisando o orçamento...")

if  somaLista > valor:
    print("O preço dos produtos passou do seu orçamento!")
    listaPC.clear()
    print("2 itens foram removidos: ",listaPC)
else:
    print("Preço compatível com o orçamento! Compra efetuada.")


