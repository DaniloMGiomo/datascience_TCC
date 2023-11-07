import pandas as pd
import solara
import plotly.express as px

github_url = "https://github.com/DaniloMGiomo/datascience_TCC"

eva_med = pd.read_parquet("./ensino/fundamental_medio/evasao_escolar_2022.parquet")
eva_sup = pd.read_parquet("./ensino/superior/EVASAO_CADASTRO_CURSOS_2022.parquet")

columns_med = ["NO_ENTIDADE", "DS_ENDERECO", "NU_ENDERECO", "CO_CEP", "QT_MAT_MED"]
columns_sup = ["vagas"]
x_med = solara.reactive("NO_ENTIDADE")
x_sup = solara.reactive("vagas")


@solara.component()
def Page():
    med = px.scatter(
        eva_med,
        x_med.value,
        "QT_evasao",
        title="Evasão Escolar Ensino Fundamental/Médio",
        labels={
            "QT_evasao": "Evasão",
            "NO_ENTIDADE": "Instituição",
            "DS_ENDERECO": "Endereço",
            "NU_ENDERECO": "Número",
            "CO_CEP": "CEP",
            "QT_MAT_MED": "Matriculas",
        },
    )
    sup = px.scatter(
        eva_sup,
        x_sup.value,
        "desistentes",
        title="Desistentes Ensino Superior",
        labels={"CO_IES": "IES", "vagas": "Vagas", "desistentes": "Desistentes"},
    )

    with solara.Column():
        solara.Title("Análise de Dados")
        with solara.Sidebar():
            with solara.Card():
                with solara.Column():
                    solara.Button(
                        label="Código fonte",
                        icon_name="mdi-github-circle",
                        attributes={"href": github_url, "target": "_blank"},
                        text=True,
                        outlined=True,
                    )
        with solara.Card("Gráficos"):
            solara.FigurePlotly(med)
            solara.Select(label="Coluna X", value=x_med, values=columns_med)

            solara.FigurePlotly(sup)


@solara.component
def Layout(children):
    return solara.AppLayout(children=children)
