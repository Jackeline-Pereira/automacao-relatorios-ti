# 📊 Automação de Relatórios Executivos de TI (ETL em Python)

Pipeline de automação desenvolvido em Python para extrair, limpar, analisar dados brutos de chamados de suporte técnico (Helpdesk) e gerar relatórios executivos consolidados em Excel.

## 🎯 O Problema Resolvido
Em ambientes corporativos, relatórios extraídos de sistemas de chamados frequentemente contêm registos duplicados, campos vazios e falta de métricas consolidadas, exigindo horas de trabalho manual em planilhas. Este projeto automatiza todo esse fluxo em segundos.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Pandas**: Manipulação, limpeza e agregação de dados.
* **Openpyxl**: Exportação e estruturação de relatórios em múltiplas abas no Excel (`.xlsx`).
* **NumPy**: Geração de massa de dados simulada para testes.

## ⚙️ Como Funciona o Pipeline (ETL)
1. **Extração (`Extract`)**: Leitura automatizada da base bruta (`chamados_ti.csv`).
2. **Tratamento e Limpeza (`Transform`)**:
   * Remoção de chamados duplicados por ID.
   * Tratamento de valores nulos (preenchimento de setores em branco e imputação da média para tempos de atendimento ausentes).
3. **Análise e Geração de KPIs**:
   * Cálculo do volume total de chamados e tempo médio de resolução por setor.
   * Filtragem automática de **Alertas Críticos** (chamados de prioridade *Alta* ou *Urgente* ainda pendentes).
4. **Exportação (`Load`)**: Geração do ficheiro `Relatorio_Executivo_TI.xlsx` dividido em três abas: *Resumo por Setor*, *Alertas Críticos* e *Base Tratada Completa*.

## 🚀 Como Executar o Projeto
1. Clone este repositório:
   ```bash
   git clone [https://github.com/Jackeline-Pereira/automacao-relatorios-ti.git](https://github.com/Jackeline-Pereira/automacao-relatorios-ti.git)
