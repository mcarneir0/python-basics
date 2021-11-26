# Abrindo e Fechando arquivos

"""
Podemos criar arquivos novos ou abrir arquivos já existentes utilizando a função open.
Ela possui 2 argumentos: o caminho do arquivo e o modo de operação.
"""

"""
Modo     Símbolo            Descrição

read	    r	    lê um arquivo existente
write	    w	    cria um novo arquivo
append	    a	    abre um arquivo existente para adicionar informações ao seu final
update	    +	    ao ser combinado com outros modos, permite alteração de arquivo já existente
                    (ex: r+ abre um arquivo existente e permite modificá-lo)


Após abrirmos (ou criarmos) um arquivo, podemos realizar diversas operações.
Ao final de todas elas, devemos fechar o nosso arquivo usando a função close.
Essa etapa é importante por 2 motivos:
    1.  Se alteramos o arquivo mas não o fechamos, as alterações não serão salvas;
    2.  Se esquecemos de fechar um arquivo, outros programas podem ter problemas ao acessá-lo.
"""


# Abrir ou criar um arquivo:
arquivocriado = open("criado.txt", "w")

"""
A linha de comando acima abre (ou cria se não existe) um arquivo chamado "criado.txt" para escrita ("w", de write)
e guarda na variável "arquivocriado" as informações para manipulá-lo.
"""

arquivolido = open("teste.txt", "r")

"""
A linha acima lê ("r", de read) um arquivo já existente chamado "teste.txt"
e guarda na variável "arquivolido" as informações para manipulá-lo.
"""


# Ler um arquivo

dados = arquivolido.read()  # A função read() retorna todo o conteúdo do arquivo como uma string.
print(dados)


# Escrever em um arquivo

arquivocriado.write("linha 1")
arquivocriado.write("linha 2")
arquivocriado.write("linha 3")
# A função write() escreve diretamente no arquivo.


# Fechar o arquivo

"""
Essa etapa é muito importante para garantir a integridade dos novos dados no arquivo.
As modificações são salvas somente ao fechar o arquivo.
"""

arquivocriado.close()
arquivolido.close()


# Comando with

"""
Um jeito mais inteligente de se trabalhar com arquivos é utilizar a sintaxe do "with".
Ele garante que após a finalização do bloco, o arquivo será fechado.
"""

with open('teste.txt', 'r') as arquivolido:
    dados = arquivolido.read()
    print(dados)


# É possível ler o arquivo linha a linha, como no exemplo:

with open('teste.txt', 'r') as arquivolido:
    linha = arquivolido.readline()
    while linha != '':
        print(linha, end='')    # end='' significa não pular linha automaticamente ao final do print
        linha = arquivolido.readline()

# OU

with open('teste.txt', 'r') as arquivolido:
    for linha in arquivolido:
        print(linha, end='')    # end='' significa não pular linha automaticamente ao final do print


# O mesmo pode ser feito para escrever no arquivo:
with open('teste.txt', 'r') as arquivolido:
    with open('copiateste.txt', 'w') as arquivocriado:
        for linha in arquivolido:
            arquivocriado.write(linha)

# No comando acima, as linhas do arquivo "teste.txt" são copiadas e salvas no arquivo "copiateste.txt".
