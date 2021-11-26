import csv

"""
O formato CSV (Comma Separated Values, ou Valores Separados por Vírgula)
é um arquivo de texto que representa dados em forma de tabela de forma simples.

Existe um módulo em Python para manipular arquivos CSV.
Todo programa que for utilizar o módulo CSV deverá importá-lo em seu início através do comando: import csv
"""

with open('tabelaExemplo.csv', 'w') as arquivo:
    escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')  # criando um escritor
    lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    escritor.writerows(lista)   # writerows escreve cada "sublista" da lista como uma linha

with open('tabelaExemplo.csv', "r") as arquivo:
    leitor = csv.reader(arquivo, delimiter=';', lineterminator='\n')    # criando um leitor
    print("O conteúdo do arquivo é:")
    print(leitor)
    for linha in leitor:
        print(linha)


# DictReader e DictWriter

"""
Podemos também trabalhar com dicionários,
nos quais a primeira linha é lida como a chave e as demais são os respectivos valores:
"""

with open('users.csv', 'w', newline='') as csvfile:
    chaves = ['first_name', 'last_name']    # definimos o cabeçalho
    writer = csv.DictWriter(csvfile, fieldnames=chaves)     # especificamos o cabeçalho

    writer.writeheader()    # escrevemos o cabeçalho
    writer.writerow({'first_name': 'Senhor', 'last_name': 'Batata'})    # escrevemos linhas com as chaves e valores
    writer.writerow({'first_name': 'Will', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Elon', 'last_name': 'Musk'})

with open('users.csv', 'r') as csvfile:
    leitor = csv.DictReader(csvfile)  # a primeira linha é lida como um cabeçalho
    for linha in leitor:
        print(linha['first_name'])     # podemos chamar um valor específico de cada linha pela chave no cabeçallho
