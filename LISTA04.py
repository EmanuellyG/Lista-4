
import pandas as pd
import streamlit as st
import ipeadatapy as ip
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Lista de Exercícios 4",
    page_icon="👋",
)


st.subheader("Uso do Pandas para análise de dados em CSV")

code = '''
df = pd.read_csv("https://raw.githubusercontent.com/EmanuellyG/projeto1/main/projetos-1.csv", sep=";") 
st.dataframe(df.head(23))
'''
st.code(code, language='python')

df = pd.read_csv("https://raw.githubusercontent.com/EmanuellyG/projeto1/main/projetos-1.csv", sep=";") 

st.dataframe(df.head(23))

st.write("Uso do `st.experimental_data_editor()` para edição do dataframe na tela")

code = '''df = pd.read_csv(arquivo, sep=';') 
df.head(23)'''
st.code(code, language='python')

edited_df = st.experimental_data_editor(df, num_rows="dynamic")

"---"  

st.write("Usando `st.checkbox()` para deixar o leitor escolher se vai mostrar a tabela ou não")

code = '''
if st.checkbox('Mostrar dataframe'):
    # usando o streamlit para apresentar como df dinâmico e formatação adicional (max)
    st.dataframe(df.style.highlight_max(axis=0)) 
    '''
st.code(code, language='python')

if st.checkbox('Mostrar dataframe'):
    # usando o streamlit para apresentar como df dinâmico e formatação adicional (max)
    st.dataframe(df.style.highlight_max(axis=0)) 

"---"    

st.write("Adicionando nova linha")

code = '''
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.write(df)
'''
st.code(code, language='python')

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.write(df)

"---"  

st.write("Apresentação da soma dos valores de cada projeto agrupado por ano")

code = '''st.write(df.groupby('ano').sum())'''
st.code(code, language='python')

st.write(df.groupby('ano').sum())

"---"  

st.write("Geração do gráfico de dispersão cruzando os dados do `Projeto1` e `Projeto2`")

code = '''
fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', ax=ax)
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', ax=ax)
st.pyplot(fig)

"---"  

st.write("Criação do gráfico do tipo histograma com os dados do `Projeto 1` e `Projeto4`")

code = '''

fig, ax = plt.subplots()
df["Projeto1"].plot(kind='hist', ax=ax)
# Exibição do gráfico no Streamlit
#st.pyplot(fig)

#fig, ax = plt.subplots()
df["Projeto4"].plot(kind='hist', ax=ax)
# Exibição do gráfico no Streamlit
st.pyplot(fig)
'''
st.code(code, language='python')


fig, ax = plt.subplots()
df["Projeto1"].plot(kind='hist', ax=ax)
# Exibição do gráfico no Streamlit
#st.pyplot(fig)


#fig, ax = plt.subplots()
df["Projeto4"].plot(kind='hist', ax=ax)
# Exibição do gráfico no Streamlit
st.pyplot(fig)
