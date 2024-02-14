#uma string 
frase = "Oi, como você está?"

#uma lista
frutas = ['amora', 'laranja', 'uva', 'melância']

#outra lista
ni = [1,2,3,4,5,6,7,8,9,10]

#imprime a primeira letra da frase
print(frase[0])

#imprime o primeiro item da lista
print(frutas[0])

#imprime o segundo item da lista
print(frutas[1])

#imprime a lista toda
print(frutas)

#imprime o tipo que está contido na variável 
print(type(frutas))

#imprime de 0 até o item 4
print(frase[0:4])

#cortando a frase
print(frase[4:19])

#pulando de dois em dois
print(frase[5:19:2])

#mais um pulando de dois
print(ni[0:10:2])

#só mais um
print(ni[1:10:2])

#imprimindo o último item da lista
print(frutas[-1])

#imprimindo com passo negativo, de trás para frente
print(frutas[-1:-4:-1])

#com números
print(ni[-1:-11:-1])

#de outra forma
print(ni[::-1])

#adicionar uma fruta na lista
frutas.append('melão')
print(frutas)

frutas.append('banana')
print(frutas)

frutas.remove('laranja')
print(frutas)

#limpa toda a lista
#frutas.clear()
#print(frutas)

#inserir em determinado índice
frutas.insert(2, 'pêssego')
frutas.insert(5, 'cereja')
print(frutas)

#mudar um nome
frutas[0] = 'ameixa'
print(frutas)

#contar
print(frutas.count('pêssego'))

#verificando o tamanho da lista ou string
print(len(frase))
print(len(frutas))

#método pop, imprime e tira o último item da lista
print(frutas.pop())
print(frutas.pop())
print(frutas)

#imprimindo tudo em minúsculo
print(frase.lower())
print(frase)

#transformando string em lista
print(frase.split(','))
frase_lista = frase.split(',')
print(frase_lista[0])
print(frase_lista[1])
print(type(frase_lista))