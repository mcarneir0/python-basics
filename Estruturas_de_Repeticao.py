# While

"""
O while possui uma expressão, e é executado caso ela seja verdadeira.
Ao final de sua execução, ele torna a testar a expressão
Caso ela seja verdadeira, ele repete sua execução.
"""

horario = int(input('Qual horario é agora? '))

# Testando a condição uma única vez com o if:
if 0 < horario < 6:
    print('Você está no horario da madrugada')
else:
    print('Você nao está no horario da madrugada')

# Testando a condição em loop com o while:
while 0 < horario < 6:
    print('Você está no horario da madrugada')
    horario = horario + 1
else:
    print('Você nao está no horario da madrugada')

# O while permite continuar decrementando o número de pipocas até chegar em 0:
num_pipocas = int(input('Digite o numero de pipocas: '))

while num_pipocas > 0:
    print('O numero de pipocas é: ', num_pipocas)
    num_pipocas = num_pipocas - 1


# Aplicações do While #


# Validação de entrada

"""
Uma utilidade interessante do while é obrigar o usuário a digitar apenas entradas válidas.
O exemplo abaixo só sai do loop quando o usuário digitar "OK":
"""

resposta = input('Digite OK: ')
while resposta != 'OK':
    resposta = input('Não foi isso que eu pedi, digite OK: ')


# Contador

"""
Todo tipo de código que deve se repetir várias vezes pode ser feito com o while.
Nestes casos, é normal utilizar um contador
"""

contador = 0    # Declaramos um contador como 0:
numero = int(input('Digite um numero: '))   # Definimos o número de repetições:

# Rodamos o while até o contador se igualar ao número de repetições:
while contador < numero:
    print(contador)
    contador = contador + 1


# Break

# Um jeito de forçar um loop a ser interrompido é utilizando o comando 'break'
while True:
    resposta = input('Digite OK: ')
    if resposta == 'OK':
        break
