# Projeto de Análise de Dados - Ficha de Pacientes

Este projeto realiza a transformação e análise de dados de pacientes, utilizando o DBT (Data Build Tool) para processar e transformar os dados em um banco SQLite. O projeto inclui o carregamento de dados, a criação de tabelas e agregações, com base nas variáveis de saúde, socioeconômicas e outras condições. 
Este README fornece um guia completo sobre como o projeto está estruturado, como configurar o ambiente e como rodar o projeto, desde o carregamento de dados até a execução das transformações DBT. Este projeto foi desenvolvido para atender aos requisitos do teste DIT, com foco em análise de dados, manipulação de informações e uso de ferramentas como DBT e SQLite para processamento e transformação de dados.

## Estrutura do Projeto

Este projeto é estruturado da seguinte forma:

dados_ficha_a_desafio/ │ 

   ├── data/ # Diretório contendo os dados brutos (CSV) │
   
     └── dados_ficha_a_desafio.csv # Arquivo de dados original │
    ├── dbt_project/ # Diretório DBT │ 
    
      ├── models/ # Modelos DBT de transformação │ │ 
      
          ├── agregacao_bairro_frequenta_escola.sql # Modelo de agregação por bairro e frequenta escola │ │ 
          
          ├── perfil_respondentes_transformado.sql # Modelo de agregação por id_paciente e ano-mês │ 
          
          │ └── agregacao_sexo_faixa_etaria.sql # Modelo de agregação por sexo e faixa etária │ 
          ├── dbt_project.yml # Arquivo de configuração do projeto DBT │ 
          ├── profiles.yml # Arquivo de configuração de conexão com o banco de dados SQLite │ 
          
     ├── src/ # Scripts Python utilizados no projeto │ 
          ├── clean_data.py # Script para limpar e tratar os dados │ 
          ├── load_data.py # Script para carregar os dados no banco de dados SQLite │ 
          └── analyze_data.py # Script para análise exploratória dos dados e geração de insights │ 
    ├── requirements.txt # Arquivo de dependências do projeto (Python) 
    ├── README.md # Documento com informações sobre o projeto 
    └── .gitignore # Arquivo para ignorar arquivos desnecessários (por exemplo, dados sensíveis)



### 1. **data/**
Este diretório contém os dados brutos que serão carregados e transformados. O arquivo CSV `dados_ficha_a_desafio.csv` contém as informações dos pacientes.

### 2. **dbt_project/**
O diretório DBT contém todos os modelos de transformação e configurações do DBT para processar os dados.

- **models/**: Contém os arquivos SQL com os modelos DBT que realizam a transformação dos dados. Exemplo de modelos:
  - `agregacao_bairro_frequenta_escola.sql`: Agregação de dados por bairro e frequência escolar, com variáveis de transporte e meios de comunicação.
  - `perfil_respondentes_transformado.sql`: Agregação dos dados de saúde por id_paciente e ano-mês.
  - `agregacao_sexo_faixa_etaria.sql`: Agregação dos dados de saúde por sexo e faixa etária.

- **dbt_project.yml**: Arquivo de configuração do projeto DBT.
- **profiles.yml**: Arquivo de configuração para conectar ao banco de dados SQLite. Define o caminho do banco de dados e configura a conexão para o DBT.

### 3. **src/**
Este diretório contém os scripts Python usados no projeto para carregar, limpar e analisar os dados.

- **clean_data.py**: Script que realiza o pré-processamento dos dados, como tratamento de valores nulos, remoção de outliers e transformação de colunas (como listas para strings).
- **load_data.py**: Script que carrega os dados CSV no banco de dados SQLite.
- **analyze_data.py**: Script de análise exploratória dos dados para gerar insights sobre as variáveis e condições de saúde.

### 4. **requirements.txt**
Este arquivo lista as dependências necessárias para rodar os scripts Python, como `pandas`, `sqlalchemy`, `sqlite3`, entre outras.

### 5. **.gitignore**
Este arquivo garante que arquivos desnecessários (como dados sensíveis ou arquivos temporários) não sejam enviados para o repositório do GitHub.

---

## Como Rodar o Projeto

### 1. **Configuração do Ambiente**
Antes de rodar o projeto, crie e ative um ambiente virtual para isolar as dependências:

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate


2. Instalar as Dependências
Instale as dependências do projeto usando o pip:

pip install -r requirements.txt


