import streamlit as st 
import requests
from datetime import datetime

def obterCotacaoSimples(par):
    url = f'https://economia.awesomeapi.com.br/json/last/{par}'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = par.replace('-', '')
        return float(dados[chave]['bid'])
    return 0.0

st.subheader('Cotaçao em Destaque')

col1,col2,col3 = st.columns(3)

cotacaoEUA = obterCotacaoSimples('USD-BRL')
cotacaoEUR = obterCotacaoSimples('EUR-BRL')
cotacaoBTC = obterCotacaoSimples('BTC-BRL')

with col1:
    st.metric('Dolar (USD)', f'R$ {cotacaoEUA:.4f}')


with col2:
    st.metric('Euro (EUR)', f'R$ {cotacaoEUR:.4f}')


with col3:
    st.metric('Bitcoin (BTC)', f'R$ {cotacaoBTC:.4f}')


def getCotacaoBid(par):
    url = f'https://economia.awesomeapi.com.br/json/last/{par}'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados[par.replace('-', '')]['bid']
    return None 

st.title('Menu Fincanceiro V2')

tabCotacao, tabconversor, tabhistorico = st.tabs(
    ['Cotação Atual','Conversor','Historico']
)

with tabCotacao:
    st.header('Cotação em tempo real')
    cotacao = getCotacaoBid('USD-BRL')

    if cotacao:
        st.success(f' 1 USD = R$ {float(cotacao):.4f}')
    else:
        st.warning('Falha ao objer dados da API')

with tabconversor:
    st.header('Conversor de moedas')

    valor = st.number_input('valor em USD', min_value=0.0, value=100.00, step=10.00)

    if st.button('Converter'):
        cotacao = getCotacaoBid('USD-BRL')
        if cotacao:
            resultado = float(valor) * float(cotacao)
            st.success(f'{resultado:.4f}')

st.divider()

def dataCompleta(par):
    url = f'https://economia.awesomeapi.com.br/json/last/{par}'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = par.replace('-','')
        return dados[chave]
    return None 

st.header('Dados de Referencia')
st.divider()

dados_usd = dataCompleta('USD-BRL')

if dados_usd:
    st.subheader(f"Cotação {dados_usd['name']}")

    col_h,col_l = st.columns(2)

    with col_h:
        st.metric('Maximo (High)', dados_usd['high'])

    with col_l:
        st.metric('Mínimo (Low)', dados_usd['low'])

    st.divider()
    st.info(f"Dados atualizados na API em: {dados_usd['create_date']}")

