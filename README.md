ChatPDF é uma aplicação inovadora projetada para analisar documentos PDF utilizando a API da OpenAI e a biblioteca LangChain e streamlit para o frontend. Esta aplicação oferece uma interface amigável e poderosa para extrair, processar e interagir com dados contidos em arquivos PDF, transformando a maneira como você gerencia e utiliza informações de documentos.

Funcionalidades Principais
Análise de PDF:

Utiliza a API da OpenAI para realizar análises profundas e extrair informações relevantes de arquivos PDF.
Capacidade de entender e processar textos complexos, tabelas e gráficos contidos nos PDFs.
## ChatPDF
```
├── .env                 # Environment variables
├── .gitignore           # Git ignore file
├── configs.py           # Configuration settings
├── Home.py              # Main application file
├── login_page.py        # Login page script
├── requirements.txt     # Python dependencies
├── config.yaml          # Gerencia usuarios
├── utils.py             # Utility functions
└── pages                # Additional pages for the application
    ├── 01_Debug.py      # Debug page
    └── 02_configuration.py  # Configuration page
```
Commandos para um Quickstart
##Clonar o repositorio
git clone git@github.com:quarentei/ChatPDF.git

##Virtualização
python3 -m venv .venv

##Dependencias
pip install -r requirements.txt

##.env
Crie o arquivo da variavel de ambiente - (coloque sua chave da open ai)

## Altere o arquivo config.yaml com sua informação para acessar o APP

Rode o comando 
"streamlit run Home.py"
