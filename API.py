"""
É importante estabelecer uma linguagem comum para que todos consigam consumir dados.

Essa "linguagem comum" é o que chamamos de API: Application Programming Interface.
A organização que disponibiliza os dados estabelece algumas "regrinhas" para fazermos requisições,
e em contrapartida ela garante que os recursos fornecidos também seguirão certos padrões,
facilitando a vida dos programadores.
"""

#   URI base

"""
Várias APIs fornecem um "endereço base". Todas as suas requisições incluirão esse endereço,
e ao final dele nós colocamos detalhes específicos para cada um dos recursos disponíveis.

Por exemplo, na AlphaVantage (https://www.alphavantage.co/),
uma API de dados de bolsas de valores e criptomoedas, a URI base é:
"""
URI_base = "https://www.alphavantage.co/query?"

"""
Após a interrogação nós colocaremos os campos para nossa consulta.
Por exemplo, para fazer uma consulta sem autenticação para valores da IBM, de 5 em 5 minutos,
o endereço completo fica:
"""
request = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"

"""
Note o formato com &NomeDoCampo=ValorDoCampo. Ele é bastante comum.
Outro formato bastante comum é o de "subdiretórios". Um exemplo é a PokéAPI. A URI base é:
"""
Poke_base = "https://pokeapi.co/api/v2/"

"""
Para procurar por pokémons, adicionamos pokemon/.
Em seguida, podemos colocar números (índices) ou nomes de Pokémon, como:
"""
Poke_busca = "https://pokeapi.co/api/v2/pokemon/ditto/"
Poke_busca2 = "https://pokeapi.co/api/v2/pokemon/25"

"""
Se ao invés de pokémons estivéssemos interessados em tipos de pokémon,
usaríamos types/ e o nome ou índice do tipo desejado:
"""
Poke_tipo = "https://pokeapi.co/api/v2/type/ghost"


#   Formato

##  Tipo de Dado

"""
Algumas APIs possuem formatos fixos de dados. Outros permitem que você escolha.
É comum, por exemplo, que uma API permita que você escolha entre JSON, XML, CSV e/ou outros formatos.
"""

##  Schema

"""
É bastante comum que as APIs disponibilizem um "modelo" genérico de como será formatado o seu JSON, XML etc
para que os desenvolvedores saibam quais campos esperar e quais tipos de dados serão possíveis para cada campo.
Por exemplo:

{
    'nome':string,
    'pontuacao':integer
}
"""

#   Autenticação

"""
Outro aspecto importante é a autenticação. Enquanto algumas APIs são grátis, outras são pagas.
Ainda temos algumas híbridas: você pode gratuitamente acessar certos recursos, ou consumir um certo volume de dados,
e acima disso você deverá pagar. Os dois modelos mais comuns de autenticação:

    Chave: ao fazer seu registro, você recebe uma chave que será inclusa na requisição.
    
    OAuth: um esquema um pouco mais complexo onde são combinados códigos de autorização, identificação do cliente
    e segredo do cliente em um POST, e o servidor cria uma sessão por um tempo limitado e fornece o ID da mesma.
    APIs de gigantes da internet (como Google e Facebook) costumam usar esse modelo.
"""

#   Rate Limiting

"""
Um dado parcialmente relacionado ao item anterior. As APIs costumam limitar o número de requisições que você pode fazer
em um instante de tempo (3 requisições por minuto, 10000 requisições por dia etc). Temos dois motivos:

    Segurança: evitar uma sobrecarga no servidor deles que possa indisponibilizar a API para todos os usuários.
    
    Venda de planos: várias APIs pagas possuem diferentes planos de pagamento. Os planos mais caros costumam permitir
    mais requisições do que os mais em conta ou gratuitos.
"""

#   Wrappers

"""
Algumas APIs possuem tantas buscas diferentes e os resultados podem ser tão complexos
que mesmo vindo em formatos simples como JSON pode ser um pouco trabalhoso montar as requisições
e isolar os dados que queremos. Por conta disso, frequentemente são fornecidas wrapper libraries:
bibliotecas escritas em linguagens de programação específicas que já trazem classes e funções prontas para fazer
requisições automaticamente e já quebrar o resultado em objetos fáceis de serem utilizados.
Elas também costumam oferecer alguns benefícios adicionais, como caching:
de tempos em tempos a base de dados é totalmente ou parcialmente baixada por completo e salva localmente,
o que ajuda a economizar requisições e, consequentemente, uso de dados
(bastante útil considerando em usuários de dispositivos móveis, por exemplo).
"""

#   Sandbox

"""
Várias APIs possuem no mesmo site de sua documentação uma área conhecida como sandbox,
onde você pode simular requisições no próprio navegador e ver não só a resposta formatada,
como informações sobre como montar aquela requisição em software.
"""


#   Consumindo APIs em Python

"""
As APIs são meios de nos conectarmos a recursos na internet. Você irá construir a lógica para decidir
o que você irá buscar/consultar, montará uma string seguindo o formato indicado pela documentação da API.
Em seguida você tratará a resposta de acordo:

    Se for JSON, utilize o método json da própria requests.
    Se for CSV, utilize o módulo CSV como visto no Arquivos_CSV.py.
    Se for XML, podemos utilizar o módulo BeautifulSoup, que não será estudado aqui.
    Para outros formatos, provavelmente a solução mais fácil será baixar um módulo preparado para lidar com eles.
"""

#   Extra

"""
Tem boas ideias e gostaria de saber se existe uma boa API para ajudar?
Confira alguns bons repositórios de API organizados por categoria:
"""
link1 = "https://github.com/n0shake/public-apis"
link2 = "https://github.com/public-apis/public-apis"
link3 = "https://any-api.com/"
