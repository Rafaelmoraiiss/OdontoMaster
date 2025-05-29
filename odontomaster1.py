import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path
BASE_DIR = Path(__file__).parent

# Leitura da planilha
file = BASE_DIR/"Pacientes.xlsx"
df = pd.read_excel(file)


# Estilo dos gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


# Copiar o DataFrame para trabalhar com segurança
df_copy = df.copy()

# Padronização de strings
df_copy['Tipo de Consulta'] = df_copy['Tipo de Consulta'].str.strip().str.capitalize()
df_copy['Sexo'] = df_copy['Sexo'].str.strip().str.capitalize()
df_copy['Auxiliar Presente'] = df_copy['Auxiliar Presente'].str.strip().str.capitalize()
df_copy['Motivo do Procedimento'] = df_copy['Motivo do Procedimento'].str.strip().str.capitalize()

# Classificação Estético vs Funcional
def classificar_motivo(motivo):
    if pd.isnull(motivo):
        return 'Não classificado'
    elif 'estética' in motivo.lower():
        return 'Estético'
    else:
        return 'Funcional'

df_copy['Classificação Motivo'] = df_copy['Motivo do Procedimento'].apply(classificar_motivo)

# Faixa Etária
bins = [0, 17, 30, 45, 60, 75, 100]
labels = ['0-17', '18-30', '31-45', '46-60', '61-75', '76+']
df_copy['Faixa Etária'] = pd.cut(df_copy['Idade'], bins=bins, labels=labels, right=False)

#Grafico 1 
Grafico1 = plt.figure(figsize=(8, 5))
sns.countplot(data=df_copy, x="Tipo de Consulta")
plt.title("Proporção de Consultas: Inicial vs Retorno")
plt.xlabel("Tipo de Consulta")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()
st.pyplot(Grafico1)

#Grafico 2 
Grafico2 = plt.figure(figsize=(12, 6))
sns.countplot(data=df_copy, y="Procedimento", hue="Tipo de Consulta")
plt.title("Tipo de Consulta por Procedimento")
plt.xlabel("Número de Consultas")
plt.ylabel("Procedimento")
plt.tight_layout()
plt.show()
st.pyplot(Grafico2)

#Grafico 3
Grafico3 = plt.figure(figsize=(12, 6))
sns.countplot(data=df_copy, y="Procedimento", hue="Faixa Etária")
plt.title("Procedimentos por Faixa Etária")
plt.xlabel("Número de Procedimentos")
plt.ylabel("Procedimento")
plt.tight_layout()
plt.show()
st.pyplot(Grafico3)

#Grafico 4
Grafico4 = plt.figure(figsize=(8, 5))
sns.countplot(data=df_copy, x="Classificação Motivo", hue="Sexo")
plt.title("Classificação Estética vs Funcional por Sexo")
plt.xlabel("Classificação do Procedimento")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()
st.pyplot(Grafico4)

#Grafico 5 
Grafico5 = plt.figure(figsize=(10, 6))
sns.countplot(data=df_copy, y="Procedimento", hue="Auxiliar Presente")
plt.title("Presença de Auxiliar por Tipo de Procedimento")
plt.xlabel("Número de Procedimentos")
plt.ylabel("Procedimento")
plt.tight_layout()
plt.show()
st.pyplot(Grafico5)

# Agora vou fazer o Dashboard 

import streamlit as st
import pandas as pd

st.title("dashboard de pacientes")
df = pd.read_excel(file)
st.dataframe(df)
