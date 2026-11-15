import pandas as pd
import numpy as np

# Simulando dados brutos de chamados de suporte de TI
np.random.seed(42)
n_linhas = 50

dados = {
    'ID_Chamado': range(1001, 1001 + n_linhas),
    'Setor': np.random.choice(['Financeiro', 'RH', 'Comercial', 'Producao'], n_linhas),
    'Prioridade': np.random.choice(['Baixa', 'Media', 'Alta', 'Urgente'], n_linhas, p=[0.4, 0.3, 0.2, 0.1]),
    'Status': np.random.choice(['Resolvido', 'Pendente', 'Em Andamento'], n_linhas, p=[0.6, 0.25, 0.15]),
    'Tempo_Atendimento_Horas': np.random.randint(1, 48, n_linhas)
}

df = pd.DataFrame(dados)

# Inserindo algumas linhas duplicadas e valores nulos propositalmente para testar a nossa limpeza
df.loc[5, 'Setor'] = None
df.loc[12, 'Tempo_Atendimento_Horas'] = None
df = pd.concat([df, df.iloc[[0, 1, 2]]], ignore_index=True) # Adicionando duplicadas

df.to_csv('chamados_ti.csv', index=False)
print("✅ Ficheiro 'chamados_ti.csv' gerado com sucesso para o nosso teste!")