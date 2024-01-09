# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_data_extraction.ipynb.

# %% auto 0
__all__ = ['matriculas', 'matricula_files', 'df_matriculas', 'turmas', 'turma_files', 'df_turmas', 'componente_filename',
           'componente_url', 'df_componentes_curriculares_presenciais', 'docente_filename', 'docente_url',
           'df_docentes', 'df']

# %% ../nbs/00_data_extraction.ipynb 3
import os

import requests
import pandas as pd
import matplotlib.pyplot as plt

# %% ../nbs/00_data_extraction.ipynb 5
matriculas = {
    '2022.2': {
        'filename': 'matriculas-2022.2.csv',
        'url': 'https://dados.ufrn.br/dataset/c8650d55-3c5a-4787-a126-d28a4ef902a6/resource/b159805b-e7cb-4d71-872b-14a1a2625d7e/download/matriculas-2022.2.csv'
    },
}

"""
'2022.1': {
    'filename': 'matriculas-2022.1.csv',
    'url': 'https://dados.ufrn.br/dataset/c8650d55-3c5a-4787-a126-d28a4ef902a6/resource/c3b45170-5417-4f2a-a53e-c8edbf6c501a/download/matriculas-2022.1.csv'
},
'2021.1': {
    'filename': 'matriculas-2021-1.csv',
    'url': 'https://dados.ufrn.br/dataset/c8650d55-3c5a-4787-a126-d28a4ef902a6/resource/ffd73a99-325b-4835-9338-036be30fdec8/download/matriculas-2021-1.csv',
},
'2021.2': {
    'filename': 'matriculas-2021-2.csv',
    'url': 'https://dados.ufrn.br/dataset/c8650d55-3c5a-4787-a126-d28a4ef902a6/resource/d5a9b2ae-4bd7-4a43-b169-2f6a5c9d1379/download/matriculas-2021-2.csv',
}
"""

for semestre, matricula in matriculas.items():
    if matricula['filename'] not in os.listdir('.'):
        response = requests.get(matricula['url'], verify=False)
        with open(matricula['filename'], "wb") as file:
            file.write(response.content)

# %% ../nbs/00_data_extraction.ipynb 6
matricula_files = [matricula['filename'] for _, matricula in matriculas.items()]
df_matriculas = pd.concat((pd.read_csv(f, sep=';') for f in matricula_files), ignore_index=True)

# %% ../nbs/00_data_extraction.ipynb 9
turmas = {
    '2022.2': {
        'url': 'https://dados.ufrn.br/dataset/1938623d-fb07-41a4-a55a-1691f7c3b8b5/resource/991cb0c0-ea9d-4507-8ff2-a24b288d90b5/download/turmas-2022.2.csv',
        'filename': 'turmas-2022.2.csv',
    },
    
}

"""
'2022.1': {
    'url': 'https://dados.ufrn.br/dataset/1938623d-fb07-41a4-a55a-1691f7c3b8b5/resource/222b1028-ca3c-4acc-bfb2-fa4e45d7cd0d/download/turmas-2022.1.csv',
    'filename': 'turmas-2022.1.csv',
},
'2021.1': {
    'filename': 'turmas-2021.1.csv',
    'url': 'https://dados.ufrn.br/dataset/1938623d-fb07-41a4-a55a-1691f7c3b8b5/resource/21a54fb0-84b9-4eab-a697-9851b932729d/download/turmas-2021.1.csv',
},
'2021.2': {
    'filename': 'turmas-2022.2.csv',
    'url': 'https://dados.ufrn.br/dataset/1938623d-fb07-41a4-a55a-1691f7c3b8b5/resource/2d657f25-de50-4dd8-b3bf-e272ddc9fb27/download/turmas-2021.2.csv',
}
"""

for semestre, turma in turmas.items():
    if turma['filename'] not in os.listdir('.'):
        response = requests.get(turma['url'], verify=False)
        with open(turma['filename'], "wb") as file:
            file.write(response.content)

# %% ../nbs/00_data_extraction.ipynb 10
turma_files = [turma['filename'] for _, turma in turmas.items()]
df_turmas = pd.concat((pd.read_csv(f, sep=';') for f in turma_files), ignore_index=True)

# %% ../nbs/00_data_extraction.ipynb 12
df_turmas = df_turmas[df_turmas['situacao_turma'] == 'CONSOLIDADA']
df_turmas = df_turmas.loc[:, ['id_turma', 'siape', 'id_componente_curricular', 'ano', 'periodo']]
df_turmas.head()

# %% ../nbs/00_data_extraction.ipynb 14
componente_filename = "componentes-curriculares-presenciais.csv"
componente_url = "https://dados.ufrn.br/dataset/3fea67e8-6916-4ed0-aaa6-9a8ca06a9bdc/resource/9a3521d2-4bc5-4fda-93f0-f701c8a20727/download/componentes-curriculares-presenciais.csv"

if componente_filename not in os.listdir('.'):
    response = requests.get(componente_url, verify=False)
    with open(componente_filename, "wb") as file:
        file.write(response.content)

# %% ../nbs/00_data_extraction.ipynb 15
df_componentes_curriculares_presenciais = pd.read_csv('componentes-curriculares-presenciais.csv', sep=';')

# %% ../nbs/00_data_extraction.ipynb 17
df_componentes_curriculares_presenciais = df_componentes_curriculares_presenciais.loc[:, ['id_componente', 'nome', 'codigo', 'unidade_responsavel']]

# %% ../nbs/00_data_extraction.ipynb 19
docente_filename = "docentes.csv"
docente_url = "https://dados.ufrn.br/dataset/8bf1a468-48ff-4f4d-95ee-b17b7a3a5592/resource/6a8e5461-e748-45c6-aac6-432188d88dde/download/docentes.csv"

if docente_filename not in os.listdir('.'):
    response = requests.get(docente_url, verify=False)
    with open(docente_filename, "wb") as file:
        file.write(response.content)

# %% ../nbs/00_data_extraction.ipynb 20
df_docentes = pd.read_csv('docentes.csv', sep=';')

# %% ../nbs/00_data_extraction.ipynb 21
df_docentes = df_docentes.loc[:, ['siape', 'nome']]

# %% ../nbs/00_data_extraction.ipynb 23
df = df_matriculas.merge(df_turmas, how='inner', on='id_turma')

# %% ../nbs/00_data_extraction.ipynb 25
df = df.merge(df_componentes_curriculares_presenciais, how='inner', left_on='id_componente_curricular', right_on='id_componente')

# %% ../nbs/00_data_extraction.ipynb 27
df = df.merge(df_docentes, how='inner', on='siape', suffixes=('_componente', '_docente'))

# %% ../nbs/00_data_extraction.ipynb 29
df.to_csv('turma_matricula_docente_filtrados.csv')
