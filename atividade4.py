#Faça 4 listas:
# A.Filmes 
# B.Jogos
# C.Livros
# D.Esporte 
# Cada lista deve ter no mínimo 2 itens.
# a.Crie uma lista das 4 listas criadas acima.
# b.Acesse(mostrar)algum item da lista livros.

listaFilmes  = ["Coraline","The Conjuring"]
listaJogos   = ["Mortal Kombat","Street Fighter"]
listaLivros  = ["Maze Runner", "Anne Frank"]
listaEsporte = ["Karate","Crossfit"]
print("Lista de filmes:  ",listaFilmes)
print("Lista de jogos:   ",listaJogos)
print("Lista de livros:  ",listaLivros)
print("Lista de esportes:",listaEsporte)

listaGlobal = listaFilmes + listaJogos + listaLivros + listaEsporte
print("Listas mescladas:", listaGlobal)
