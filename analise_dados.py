import pandas as pd

print("🚀 Iniciando pipeline de automação de dados...")

# 1. EXTRAÇÃO (Leitura dos dados brutos)
df = pd.read_csv('chamados_ti.csv')
print(f"📥 Registos brutos carregados: {len(df)}")

# 2. TRATAMENTO E LIMPEZA (Data Cleaning)
# Remover linhas completamente duplicadas baseadas no ID do chamado
df_limpo = df.drop_duplicates(subset=['ID_Chamado']).copy()

# Preencher setores vazios com 'Não Informado'
df_limpo['Setor'] = df_limpo['Setor'].fillna('Não Informado')

# Preencher tempos de atendimento vazios com a média geral dos chamados
media_tempo = round(df_limpo['Tempo_Atendimento_Horas'].mean(), 1)
df_limpo['Tempo_Atendimento_Horas'] = df_limpo['Tempo_Atendimento_Horas'].fillna(media_tempo)

print(f"🧹 Dados limpos! Total de chamados únicos válidos: {len(df_limpo)}")

# 3. ANÁLISE E GERAÇÃO DE MÉTRICAS (KPIs de TI)
# Resumo por Setor: Total de chamados e tempo médio de resolução
resumo_setor = df_limpo.groupby('Setor').agg(
    Total_Chamados=('ID_Chamado', 'count'),
    Tempo_Medio_Horas=('Tempo_Atendimento_Horas', 'mean')
).reset_index()
resumo_setor['Tempo_Medio_Horas'] = resumo_setor['Tempo_Medio_Horas'].round(1)

# Filtro de Alerta: Chamados de prioridade Alta ou Urgente que ainda não foram resolvidos
chamados_criticos = df_limpo[
    (df_limpo['Prioridade'].isin(['Alta', 'Urgente'])) & 
    (df_limpo['Status'] != 'Resolvido')
]

# 4. EXPORTAÇÃO (Geração de Relatório Executivo em Excel)
nome_arquivo_saida = 'Relatorio_Executivo_TI.xlsx'

with pd.ExcelWriter(nome_arquivo_saida, engine='openpyxl') as writer:
    resumo_setor.to_excel(writer, sheet_name='Resumo por Setor', index=False)
    chamados_criticos.to_excel(writer, sheet_name='Alertas Criticos', index=False)
    df_limpo.to_excel(writer, sheet_name='Base Tratada Completa', index=False)

print(f"📊 Relatório '{nome_arquivo_saida}' gerado com sucesso!")
print(f"⚠️ Atenção: Foram identificados {len(chamados_criticos)} chamados críticos pendentes.")