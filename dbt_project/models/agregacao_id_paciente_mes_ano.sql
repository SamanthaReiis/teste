-- agregacao_id_paciente_mes_ano

WITH dados_transformados AS (
    SELECT
        p.id_paciente,
        -- Extrair o ano-mês das datas
        strftime('%Y-%m', p.data_cadastro) AS ano_mes_cadastro,
        strftime('%Y-%m', p.data_atualizacao_cadastro) AS ano_mes_atualizacao,
        strftime('%Y-%m', p.updated_at) AS ano_mes_updated,
        p.tipo,
        -- Para as outras colunas, usaremos a última atualização de cada paciente
        MAX(p.data_cadastro) AS data_cadastro_max,
        MAX(p.data_atualizacao_cadastro) AS data_atualizacao_cadastro_max,
        MAX(p.updated_at) AS updated_at_max
    FROM 
        {{ ref('perfil_respondentes') }} p  -- Referência à tabela 'perfil_respondentes'
    GROUP BY 
        p.id_paciente, ano_mes_cadastro, ano_mes_atualizacao, ano_mes_updated, p.tipo
)

SELECT
    id_paciente,
    ano_mes_cadastro,
    ano_mes_atualizacao,
    ano_mes_updated,
    tipo,
    data_cadastro_max,
    data_atualizacao_cadastro_max,
    updated_at_max
FROM dados_transformados;
