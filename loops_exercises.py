# Exercício realizado no treinamento 
# Usar loops "while" e "for" em Python
# na Microsoft Learn.
# Modifiquei adicionando um tempo 
# para apresentar os planetas digitados
# e o total de planetas.

from time import sleep


new_planets = ''
planets = []

while new_planets.lower() != 'done':
    if new_planets:
        planets.append(new_planets)
    new_planets = input('Digite um novo planeta ou done para sair: ')

for planet in planets:
    print(planet.title())
    sleep(1)
print('Total de {x} planetas.' .format(x=len(planets)))
