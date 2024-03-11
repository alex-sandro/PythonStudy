# Primeiro desafio Ok
# https://franciscofoz.medium.com/5-desafios-com-strings-para-iniciantes-em-python-81e3a5ba9cbe


titulos = """O Senhor dos Anéis
Harry Potter e a Pedra Filosofal
1984
O Lobo da Estepe
Cem Anos de Solidão
A Metamorfose
A Revolução dos Bichos
Crime e Castigo
Macunaíma"""

separar_titulos = titulos.split('\n')
#print(separar_titulos)

separar_titulos.sort()
#print(separar_titulos)

titulos_unidos = ', '.join(separar_titulos)
print(titulos_unidos)

