# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_solara.ipynb.

# %% auto 0
__all__ = ['db', 'unidade', 'componente', 'docente', 'SelectUnidade', 'SelectComponente', 'SelectDocente', 'PieChart', 'Page']

# %% ../nbs/02_solara.ipynb 3
from typing import Union, Tuple

import solara
import pandas as pd
import matplotlib.pyplot as plt

from ufrn_cheat_sheet.storage import ReadOnlyInMemorySQLite

# %% ../nbs/02_solara.ipynb 4
#| skip_exec: true
#| skip_showdoc: true
db = ReadOnlyInMemorySQLite()

# %% ../nbs/02_solara.ipynb 5
def db_get(data: Union[Tuple, solara.Reactive]):
    if data.value and isinstance(data.value, list):
        return data.value[0]

    return data.value

# %% ../nbs/02_solara.ipynb 6
unidade = solara.reactive(None)
componente = solara.reactive(None)
docente = solara.reactive(None)

# %% ../nbs/02_solara.ipynb 8
@solara.component
def SelectUnidade():
    values = db.execute_query('SELECT DISTINCT(unidade_responsavel) from data ORDER BY unidade_responsavel')
    solara.Select(label="Unidade", value=unidade, values=values)

# %% ../nbs/02_solara.ipynb 9
@solara.component
def SelectComponente():
    values = db.execute_query(
        f"""
        SELECT DISTINCT(nome_componente) from data 
        WHERE unidade_responsavel = '{db_get(unidade)}' 
        ORDER BY nome_componente
        """
    )
    solara.Select(label="Componente", value=componente, values=values)

# %% ../nbs/02_solara.ipynb 10
@solara.component
def SelectDocente():
    values = db.execute_query(
        f"""
        SELECT DISTINCT(nome_docente) from data 
        WHERE 
            unidade_responsavel = '{db_get(unidade)}' 
            AND 
            nome_componente = '{db_get(componente)}' 
        ORDER BY nome_componente
        """
    )
    solara.Select(label="Docente", value=docente, values=values)

# %% ../nbs/02_solara.ipynb 11
def PieChart():
    #solara.use_state(docente)
    
    q = f"""SELECT descricao, COUNT(*) as contagem
    FROM (
        SELECT DISTINCT discente, descricao
        FROM data
        WHERE unidade_responsavel = '{db_get(unidade)}'
        AND nome_componente = '{db_get(componente)}'
        AND nome_docente = '{db_get(docente)}'
    )
    GROUP BY descricao;
    """

    data = pd.read_sql_query(q, db.connection)

    data['porcentagem'] = (data['contagem'] / data['contagem'].sum()) * 100

    contagem_descricao = data['descricao'].value_counts()
    porcentagens = (contagem_descricao / contagem_descricao.sum()) * 100
    
    fig, ax = plt.subplots(figsize=(10, 6))
    wedges, texts, autotexts = ax.pie(porcentagens, labels=porcentagens.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))
    
    for text, autotext in zip(texts, autotexts):
        text.set(size=10)
        autotext.set(size=10)
    
    legend_labels = [f"{label}: {value}" for label, value in zip(contagem_descricao.index, contagem_descricao.values)]
    ax.legend(wedges, legend_labels, title="Descrições", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    solara.FigureMatplotlib(fig)

# %% ../nbs/02_solara.ipynb 13
@solara.component
def Page():
    with solara.AppBarTitle():
        solara.Text("UFRN Cheat Sheet")

    with solara.Column():
        with solara.Row():
            SelectUnidade()
            SelectComponente()
            SelectDocente()
        PieChart()

# %% ../nbs/02_solara.ipynb 14
Page()
