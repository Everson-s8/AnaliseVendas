# // Fazer o import da bilioteca

import pandas as pd
from twilio.rest import Client

# Conexão com o site twilio
# onde o acount_sid é o id da sua conta
# auth_token é o um codigo de autenticação que é passado para vc

account_sid = 'AC530126ebb267ebd80cb157ab3517ecb9'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)


# Fazer uma lista com os nomes dos arquivos excel
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

# Para ler o arquivo excel, para isso é necessario passar o nome correto do arquivo
# Para ir lendo os meses usa um for para pecorre a lista_meses e
# em cada mes ler o seu arquivo correspodente
# o f {} é para deixar o string dinamico, assim ele consegue inserir
# o valor passado de lista_meses correspondete em cada laço para dentro da variavel
# Exemplo:
# Primeira vez que for repetir o for
#  lista_vendas = pd.read_excel(janeiro.xlsx, na proxima vez fevereiro.xksx e assim por diante
# Agora para descobrir se existe algum valor na tabela do mes maior do que o valor desejado
# faço uma condição , passando em lista_vendas para procurar na coluna Vendas, algum valor maior
# do que o valor minimo que eu passei para o bonus. Usando o .any para fazer isso indicando
#  que vai ser algum valor na coluna "Vendas"
# Para localizar vendedor se usa um .loc que localiza na tabela[linha, coluna] o mesmo se usa em vendas
# em linhas se passa a condição assim buscando a linha que se tenha venda maior que 55mil
# .value[0] é para indicar que deseja se pegar apenas um unico valor daquilo
for mes in lista_meses:
    lista_vendas = pd.read_excel(f"{mes}.xlsx")
    if (lista_vendas["Vendas"] > 55000).any():
        vendedor = lista_vendas.loc[lista_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = lista_vendas.loc[lista_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No {mes} o Vendedor {vendedor} vendeu {vendas}, assim batendo a meta")
        message = client.messages.create(
            from_='whatsapp:number',
            body=f'"No {mes} o Vendedor {vendedor} vendeu {vendas}, assim batendo a meta"',
            to='whatsapp:number'
        )

        print(message.sid)


# message = cliente.messages.create para baixo é para fazer a conexão com o whatsapp do número
# passado pelo site e o teu número, from é o número de onde vai vim a msg do caso do servido do twilio
# to para o usuario que vc deseja que receba o número


