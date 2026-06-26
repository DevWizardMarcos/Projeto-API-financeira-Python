import streamlit as st
import requests
from pathlib import Path



def carregar_css():
    caminho_css = Path("assets/css/style.css")
    if caminho_css.exists():
        css = caminho_css.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def obter_cotacao_simples(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = par.replace("-", "")
        return float(dados[chave]["bid"])
    return 0.0

def get_cotacao_bid(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados[par.replace("-", "")]["bid"]
    return None

def data_completa(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = par.replace("-", "")
        return dados[chave]
    return None

carregar_css()

col_esq, col_centro, col_dir = st.columns([1, 2, 1])
with col_centro:
    st.image("assets/mascot.png", width=650)

st.markdown("<h1 class='titulo-principal'>Consumo de API financeira</h1>", unsafe_allow_html=True)

st.subheader("Cotação em destaque")

col1, col2, col3 = st.columns(3)

cotacao_eua = obter_cotacao_simples("USD-BRL")
cotacao_eur = obter_cotacao_simples("EUR-BRL")
cotacao_btc = obter_cotacao_simples("BTC-BRL")

with col1:
    st.metric("Dólar (USD)", f"R$ {cotacao_eua:.4f}")

with col2:
    st.metric("Euro (EUR)", f"R$ {cotacao_eur:.4f}")

with col3:
    st.metric("Bitcoin (BTC)", f"R$ {cotacao_btc:.4f}")

st.title("Menu Financeiro V2")

tab_cotacao, tab_conversor, tab_historico = st.tabs(
    ["Cotação Atual", "Conversor", "Histórico"]
)

with tab_cotacao:
    st.header("Cotação em tempo real")
    cotacao = get_cotacao_bid("USD-BRL")

    if cotacao:
        st.success(f"1 USD = R$ {float(cotacao):.4f}")
    else:
        st.warning("Falha ao obter dados da API")

with tab_conversor:
    st.header("Conversor de moedas")

    valor = st.number_input("Valor em USD", min_value=0.0, value=100.0, step=10.0)

    if st.button("Converter"):
        cotacao = get_cotacao_bid("USD-BRL")
        if cotacao:
            resultado = float(valor) * float(cotacao)
            st.success(f"R$ {resultado:.4f}")

with tab_historico:
    st.info("Aba de histórico em construção.")

st.divider()

st.header("Dados de referência")
st.divider()

dados_usd = data_completa("USD-BRL")

if dados_usd:
    st.subheader(f"Cotação {dados_usd['name']}")

    col_h, col_l = st.columns(2)

    with col_h:
        st.metric("Máximo (High)", dados_usd["high"])

    with col_l:
        st.metric("Mínimo (Low)", dados_usd["low"])

    st.divider()
    st.info(f"Dados atualizados na API em: {dados_usd['create_date']}")

