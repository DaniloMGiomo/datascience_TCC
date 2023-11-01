import pandas as pd
import solara
import plotly.express as px

eva_med = pd.read_parquet("./ensino/fundamental_medio/evasao_escolar_2022.parquet")
eva_sup = pd.read_parquet("./ensino/superior/EVASAO_CADASTRO_CURSOS_2022.parquet")

columns_med = ["NO_ENTIDADE", "DS_ENDERECO", "NU_ENDERECO", "CO_CEP", "QT_MAT_MED"]
columns_sup = ["CO_IES", "vagas"]
x_med = solara.reactive("NO_ENTIDADE")
x_sup = solara.reactive("vagas")


@solara.component()
def Page():
    med = px.scatter(eva_med, x_med.value, "QT_evasao", title="Evasão Escolar Ensino Fundamental/Médio")
    sup = px.scatter(eva_sup, x_sup.value, "desistentes", title="Desistentes Ensino Superior")
    fig = px.scatter(eva_sup, x="CO_IES", y="vagas", title="Vagas por IES")

    solara.FigurePlotly(sup)
    solara.Select(label="X-axis", value=x_sup, values=columns_sup)
    solara.FigurePlotly(fig)

    solara.FigurePlotly(med)
    solara.Select(label="X-axis", value=x_med, values=columns_med)
