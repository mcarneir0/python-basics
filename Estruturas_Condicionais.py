# If

"""
O if testa uma condição:

se ela for verdadeira, seu conteúdo é executado;
caso contrário, seu conteúdo é ignorado.
"""

idade = int(input('Digite sua idade:'))
if idade >= 12:
    print('Você pode entrar na montanha russa.')
print('Obrigado por participar.')

altura = float(input('Digite sua altura, em metros:'))
if idade >= 12 and altura >= 1.60:
    print('Você pode entrar na montanha russa.')
print('Obrigado por participar.')


# Else

"""
Em alguns casos, queremos que o programa escolha entre 2 casos mutuamente exclusivos, para isso utilizamos o else.

O else não possui condição para verificar.
O else sempre vem imediatamente após um if e é executado se o if for ignorado.
"""

idade = int(input('Digite sua idade:'))
if idade >= 12:
    resposta = input('Você gostaria de entrar nesta montanha russa?')
    if resposta == 'sim':
        print('Por favor, entre!')
    else:
        print('Ok então')
else:
    print('Você não tem idade suficiente para entrar nesse brinquedo.')


# Elif

"""
Podemos testar diversos casos mutuamente exclusivos utilizando o 'elif'.

O comando elif é a contração de "else if"
Caso um if não seja executado, você pode propor uma nova condição para ser testada.
"""

exercicios = int(input('Quantos exercícios de Python vc já fez?'))

if exercicios > 30:
    print('Já está ficando profissional!')
elif exercicios > 20:
    print('Tá indo bem, bora fazer mais alguns!')
elif exercicios > 10:
    print('Vamos tirar o atraso?')
else:
    print('Xiiii...')
