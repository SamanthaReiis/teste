import os
from sqlalchemy import create_engine
import sqlite3

# Criar a conexão com o banco de dados SQLite (ele será criado automaticamente se não existir)
conn = sqlite3.connect('dados_ficha_a_desafio.db')
cursor = conn.cursor()

# Criando a tabela id_paciente
cursor.execute('''
CREATE TABLE IF NOT EXISTS id_paciente (
    id_paciente INTEGER PRIMARY KEY,
    data_cadastro TEXT,
    data_atualizacao_cadastro TEXT,
    updated_at TEXT,
    tipo TEXT
);
''')


# Criando a tabela caract_demo
cursor.execute('''
CREATE TABLE IF NOT EXISTS caract_demo (
    id_paciente INTEGER PRIMARY KEY,
    sexo TEXT,
    raca_cor TEXT,
    identidade_genero TEXT,
    orientacao_sexual TEXT,
    nacionalidade TEXT,
    data_nascimento TEXT,
    faixa_etaria TEXT,
    FOREIGN KEY (id_paciente) REFERENCES id_paciente(id_paciente)
);
''')


# Criando a tabela cond_socio
cursor.execute('''
CREATE TABLE IF NOT EXISTS cond_socio (
    id_paciente INTEGER PRIMARY KEY,
    bairro TEXT,
    renda_familiar REAL,
    escolaridade TEXT,
    ocupacao TEXT,
    situacao_profissional TEXT,
    em_situacao_de_rua INTEGER,
    familia_beneficiaria_auxilio_brasil INTEGER,
    luz_eletrica INTEGER,
    frequenta_escola INTEGER,
    Metrô INTEGER,
    Carroça INTEGER,
    Bicicleta INTEGER,
    Animal INTEGER,
    Caminhão INTEGER,
    Carro INTEGER,
    Ônibus INTEGER,
    Alternativo INTEGER,
    Outros INTEGER,
    Marítimo INTEGER,
    Trem INTEGER,
    Rádio INTEGER,
    Revista INTEGER,
    Jornal INTEGER,
    Televisão INTEGER,
    Grupos_Religiosos INTEGER,
    Internet INTEGER,
    FOREIGN KEY (id_paciente) REFERENCES id_paciente(id_paciente)
);
''')


# Criando a tabela ind_saude
cursor.execute('''
CREATE TABLE IF NOT EXISTS ind_saude (
    id_paciente INTEGER PRIMARY KEY,
    obito INTEGER,
    possui_plano_saude INTEGER,
    vulnerabilidade_social TEXT,
    altura REAL,
    peso REAL,
    pressao_sistolica INTEGER,
    pressao_diastolica INTEGER,
    n_atendimentos_atencao_primaria INTEGER,
    n_atendimentos_hospital INTEGER,
    AIDS INTEGER,
    Alcoolismo INTEGER,
    Epilepsia INTEGER,
    Malária INTEGER,
    Transtorno_Mental INTEGER,
    Sintomático_Respiratório INTEGER,
    Intern_Psiq_Ult_12_meses INTEGER,
    Sintomático_Dermatológico INTEGER,
    Câncer INTEGER,
    Def_Visual INTEGER,
    Usuario_de_Psicofármacos INTEGER,
    Asma INTEGER,
    Def_Mental INTEGER,
    Def_Auditiva INTEGER,
    Hanseníase INTEGER,
    Violência_Doméstica INTEGER,
    Tuberculose INTEGER,
    Hipertensão INTEGER,
    Usuario_de_Drogas_Ilícitas INTEGER,
    Def_Física INTEGER,
    Diabetes INTEGER,
    Tabagismo INTEGER,
    Tentativa_de_Suicídio INTEGER,
    Gestante INTEGER,
    Farmácia INTEGER,
    Rede_Privada INTEGER,
    Hospital_Público INTEGER,
    Auxílio_Espiritual INTEGER,
    Unidade_de_Saúde INTEGER,
    FOREIGN KEY (id_paciente) REFERENCES id_paciente(id_paciente)
);
''')
# Commit para salvar as alterações
conn.commit()


# Definir a URL de conexão com o banco de dados SQLite
db_url = 'sqlite:///dados_ficha_a_desafio.db'
# Criar conexão com o banco usando SQLAlchemy
engine = create_engine(db_url)
# Carregar os dados nas tabelas SQLite
cond_socio.to_sql('cond_socio', engine, if_exists='replace', index=False)
ind_saude.to_sql('ind_saude', engine, if_exists='replace', index=False)
id_paciente.to_sql('id_paciente', engine, if_exists='replace', index=False)
caract_demo.to_sql('caract_demo', engine, if_exists='replace', index=False)


# Fechar a conexão
conn.close()
