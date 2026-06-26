<p align="center">
  <img src="BannerGit/BannerPrincipal.png" alt="Banner do Projeto API Financeira" />
</p>

Dashboard financeiro em **Python + Streamlit** para consulta de cotações em tempo real, conversão de moedas e visualização de dados de referência via **AwesomeAPI**.

## Visão geral

O **Projeto API Financeira** centraliza uma experiência simples de monitoramento cambial em uma interface web leve:

- **Cotações em destaque** (USD, EUR, BTC em BRL)
- **Cotação atual** em tempo real para USD-BRL
- **Conversor** de USD para BRL
- **Dados de referência** (máxima, mínima e timestamp da API)

> Ideal para estudo de integrações HTTP, construção de dashboards com Streamlit e prototipação de produtos financeiros.

## Preview da interface

### Tela principal

<p align="center">
  <img src="docs/preview-dashboard.png" alt="Preview do dashboard financeiro" />
</p>

> Sugestão: salve um print da aplicação em `docs/preview-dashboard.png` para exibição correta no GitHub.

## Como funciona

Fluxo atual da aplicação:

1. O usuário acessa a interface Streamlit.
2. O app consulta a **AwesomeAPI** para obter os pares desejados.
3. As cotações são renderizadas em métricas e abas.
4. No conversor, o valor em USD é multiplicado pela cotação atual USD-BRL.
5. A seção de referência exibe **high**, **low** e **create_date** retornados pela API.

## Funcionalidades

- Exibição de cotação de **Dólar (USD)**, **Euro (EUR)** e **Bitcoin (BTC)**.
- Consulta rápida de **USD-BRL** em tempo real.
- Conversão de valor em dólar para real.
- Exibição de indicadores de referência (máximo e mínimo do período).
- Interface organizada por abas para melhor navegação.

## Arquitetura da aplicação

Hoje o projeto está concentrado em um único ponto de entrada:

| Camada | Função |
|---|---|
| `main.py` | Interface Streamlit + chamadas HTTP para cotação + regra de conversão |

### Fluxo interno simplificado

```text
Streamlit UI -> requests.get() -> AwesomeAPI -> renderização de métricas/abas
```

## Tecnologias utilizadas

- **Python 3**
- **Streamlit**
- **Requests**
- **AwesomeAPI (Economia)**

## API utilizada

- [AwesomeAPI - Documentação de Moedas](https://docs.awesomeapi.com.br/api-de-moedas)

## Instalação

### Pré-requisitos

Antes de começar, garanta que você tenha instalado:

- **Python 3.10+**
- **pip**
- **Git**

### Executando localmente

```bash
# 1) Clonar repositório
git clone https://github.com/DevWizardMarcos/Projeto-API-financeira-Python.git
cd Projeto-API-financeira-Python

# 2) Ambiente virtual (recomendado)
python -m venv .venv
```

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

```bash
# 3) Instalar dependências
pip install streamlit requests

# 4) Rodar aplicação
streamlit run main.py
```

Depois, abra no navegador:
```text
http://localhost:8501
```

## Estrutura do projeto

```text
.
├── main.py
└── README.md
```

## Melhorias recomendadas (Roadmap)

- [ ] Permitir seleção dinâmica de pares (ex.: EUR-USD, BTC-USD)
- [ ] Adicionar histórico com gráfico (7d / 30d)
- [ ] Implementar cache de requisições (`st.cache_data`)
- [ ] Melhorar tratamento de falhas (timeout/retry/mensagens)
- [ ] Separar responsabilidades em módulos (`services/`, `ui/`)
- [ ] Criar `requirements.txt` e fixar versões

## Boas práticas e observações

- A aplicação depende da disponibilidade da API externa.
- Em caso de instabilidade de rede, os valores podem ficar indisponíveis temporariamente.
- Para produção, recomenda-se:
  - timeout explícito em requisições
  - fallback visual para erro
  - logs de observabilidade

## Status

Projeto em evolução, com foco em aprendizado prático de integração com APIs financeiras e construção de dashboards em Python.

## Autor

Feito por **Marcos**  
GitHub: [@DevWizardMarcos](https://github.com/DevWizardMarcos)
