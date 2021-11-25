"""
Funções são uma espécie de "subprograma".
Elas são como pequenos pedacinhos de programa que podem ser chamadas pelo nome.
Para criar uma função usamos o comando "def" e o nome da função.
"""


def hello():
    print("Olá, mundo!")


hello()
# Saída: Olá, mundo!


"""
É possível passarmos informações para uma função.
Chamamos essas informações de "parâmetros" ou "argumentos.
Na definição da função, daremos nome a esses parâmetros.
Dentro da função, eles serão tratados como se fossem variáveis.
"""


def ola(nome):
    print("Olá", nome)


aluno = "João"
ola(aluno)
# Saída: Olá, João


# A função pode receber vários parâmetros separados por vírgula.
def dadosPessoais(nome, idade, cidade):
    print("Seu nome é {}, você tem {} anos e mora em {}.".format(nome, idade, cidade))


dadosPessoais("José", 30, "Maceió")
# Saída: Seu nome é José, você tem 30 anos e mora em Maceió.


"""
Os parâmetros podem ser passados fora de ordem.
Porém, para isso precisamos explicitar qual parâmetro estamos passando,
para evitar ambiguidade ou erros de interpretação do Python.
"""

dadosPessoais(idade=56, cidade="Florianópolis", nome="Ana")
# Saída: Seu nome é Ana, você tem 56 anos e mora em Florianópolis.


# Funções com resposta

"""
Uma função pode ter uma "resposta".
Utilizamos a palavra "return" para fazer uma função retornar sua resposta.
Quando uma função retorna um valor, ela pode ser usada em
expressões matemáticas ou lógicas, ter seu valor atribuído a uma variável, etc.
"""


def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma


numeros = [1, 2, 3, 4, 5]
soma_dos_numeros = somatorio(numeros)
print("A soma dos elementos da lista vale: ", soma_dos_numeros)
# Saída: A soma dos elementos da lista vale:  15


# Funções recursivas

"""
A recursividade (ou recursão) é uma propriedade na qual uma função faz referência a si mesma.
Quando a função encontra uma nova referência, ela irá pausar sua execução atual e iniciar a execução da nova instância,
para só então retomar sua execução.
"""


def funcaoRecursiva(numero):
    if numero != 1:
        funcaoRecursiva(numero - 1)
    print(numero)


print("Testando a função recursiva:")
funcaoRecursiva(10)

"""
Note que no exemplo acima passamos 10 para a função.
Sua execução foi interrompida por uma nova chamada passando 9, depois 8, depois 7...
Ao chegar em 1, ele foge da condicional e imprime 1, encerrando a execução.
Então a instância que recebeu 2 tambem conclui sua execução, depois a chamada 3, a 4...
A 10, que foi a 1a chamada, encerra por último.
"""


print("\n# PARTE 2 #")

# Agrupando parâmetros

"""
Podemos utilizar o operador * - que, neste caso, não será uma multiplicação.
Ao colocarmos o * ao lado do nome de um parâmetro na definição da função,
estamos dizendo que aquele argumento será uma coleção. Mais especificamente, uma tupla.
Porém, o usuário não irá passar uma tupla. Ele irá passar quantos argumentos ele quiser,
e o Python automaticamente criará uma tupla com eles:
"""


def piscina(*infos):
    vol = infos[0] * infos[1] * infos[2]
    return vol


volume = piscina(5, 4, 5)
print('O volume é:', volume)


"""
Podemos utilizar o operador * na chamada da função também.
Na definição, o operador * indica que devemos agrupar itens avulsos em uma coleção.
Na chamada, ele indica que uma coleção deve ser expandida em itens avulsos:
"""


def piscina(prof, largura, comprimento):
    vol = prof * largura * comprimento
    return vol


lista = [5, 4, 5]
volume = piscina(*lista)
print('O volume é:', volume)


# Parâmetros opcionais

"""
Outra possibilidade são funções com parâmetros opcionais.
Note que isso é diferente de termos quantidade variável de parâmetros.
No caso da quantidade variável, normalmente são diversos parâmetros com a mesma utilidade
(números a serem somados, valores a serem exibidos etc),
enquanto os parâmetros opcionais são informações distintas que podem ou não ser passadas para a função.

Para criar parâmetros opcionais, usaremos **, e os parâmetros passados serão agrupados em um dicionário:
o nome do parâmetro será uma chave, e o valor será... O valor.
"""


def piscina(prof, **infos):
    vol = prof * infos['largura'] * infos['comprimento']
    return vol


volume = piscina(5, largura=4, comprimento=5)
print('O volume é:', volume)


"""
É possível que o usuário da função já tenha os dados organizados em um dicionário.
Neste caso, basta usar ** na chamada da função para expandir o dicionário em vários parâmetros opcionais:
"""


def piscina(prof, largura=4, comprimento=5):
    vol = prof*largura*comprimento
    return vol


infos = {'largura': 10, 'comprimento': 20}
volume = piscina(5, **infos)
print('O volume é:', volume)
