Sitema de consumo de API de Clima (offline)

O sistema apresentado contém código para o consumo da API, juntamente com uma interface fronted para facilitar a visualização dos dados recebidos.

Como acessar a API utilizada:
- No terminal execute: git clone https://github.com/jpsvalentim/api-meteorologica-offline.git
-Crie um ambiente virtual: python -m venv .venv
-Ative o ambiente virtual: .\.venv\Scripts\Activate.ps1
-Instale as dependências: pip install -r requirements.txt
-Execute a API: uvicorn app.main:app --reload
-Realize o teste, coloque no navegador: http://127.0.0.1:8000
-Abra a documentação interativa (opcional): http://127.0.0.1:8000/docs
-endpoint: http://127.0.0.1:8000/v1/forecast


Deixe a API rodando e abra outra aba. 
Bibliotecas necessárias para dodar o código:
-requests
-streamlit
-pandas

códigos para a instalação:
-pip install requirements
-python -m pip install requests streamlit pandas
