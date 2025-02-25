-- perfil_respondentes_transformado

WITH dados_transformados AS (
    SELECT
        p.id_paciente,
        strftime('%Y-%m', p.data_cadastro) AS ano_mes,  -- Extrai o ano-mês de data_cadastro
        -- Variáveis de saúde (AIDS, Alcoolismo, etc.)
        SUM(i.AIDS) AS soma_AIDS,
        SUM(i.Alcoolismo) AS soma_Alcoolismo,
        SUM(i.Epilepsia) AS soma_Epilepsia,
        SUM(i.Malária) AS soma_Malaria,
        SUM(i.Transtorno_Mental) AS soma_Transtorno_Mental,
        SUM(i.Sintomático_Respiratório) AS soma_Sintomatico_Respiratorio,
        SUM(i.Intern_Psiq_Ult_12_meses) AS soma_Intern_Psiq_Ult_12_meses,
        SUM(i.Sintomático_Dermatológico) AS soma_Sintomatico_Dermatologico,
        SUM(i.Câncer) AS soma_Cancer,
        SUM(i.Def_Visual) AS soma_Def_Visual,
        SUM(i.Usuario_de_Psicofármacos) AS soma_Usuario_de_Psicofarmacos,
        SUM(i.Asma) AS soma_Asma,
        SUM(i.Def_Mental) AS soma_Def_Mental,
        SUM(i.Def_Auditiva) AS soma_Def_Auditiva,
        SUM(i.Hanseníase) AS soma_Hanseníase,
        SUM(i.Violência_Doméstica) AS soma_Violencia_Domestica,
        SUM(i.Tuberculose) AS soma_Tuberculose,
        SUM(i.Hipertensão) AS soma_Hipertensao,
        SUM(i.Usuario_de_Drogas_Ilícitas) AS soma_Usuario_de_Drogas_Ilícitas,
        SUM(i.Def_Física) AS soma_Def_Fisica,
        SUM(i.Diabetes) AS soma_Diabetes,
        SUM(i.Tabagismo) AS soma_Tabagismo,
        SUM(i.Tentativa_de_Suicídio) AS soma_Tentativa_de_Suicidio,
        SUM(i.Gestante) AS soma_Gestante,
        
        -- Atendimentos
        SUM(i.n_atendimentos_atencao_primaria) AS volume_atendimentos_atencao_primaria,
        SUM(i.n_atendimentos_hospital) AS volume_atendimentos_hospital
    FROM 
        {{ ref('perfil_respondentes') }} p  -- Referência à tabela 'perfil_respondentes'
    LEFT JOIN 
        {{ ref('indicadores_saude') }} i   -- Referência à tabela 'indicadores_saude'
    ON p.id_paciente = i.id_paciente
    GROUP BY 
        p.id_paciente, ano_mes
)

SELECT
    id_paciente,
    ano_mes,
    soma_AIDS,
    soma_Alcoolismo,
    soma_Epilepsia,
    soma_Malaria,
    soma_Transtorno_Mental,
    soma_Sintomatico_Respiratorio,
    soma_Intern_Psiq_Ult_12_meses,
    soma_Sintomatico_Dermatologico,
    soma_Cancer,
    soma_Def_Visual,
    soma_Usuario_de_Psicofarmacos,
    soma_Asma,
    soma_Def_Mental,
    soma_Def_Auditiva,
    soma_Hanseníase,
    soma_Violencia_Domestica,
    soma_Tuberculose,
    soma_Hipertensao,
    soma_Usuario_de_Drogas_Ilícitas,
    soma_Def_Fisica,
    soma_Diabetes,
    soma_Tabagismo,
    soma_Tentativa_de_Suicidio,
    soma_Gestante,
    volume_atendimentos_atencao_primaria,
    volume_atendimentos_hospital
FROM dados_transformados;
