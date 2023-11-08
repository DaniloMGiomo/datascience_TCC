import pandas as pd
import numpy as np

some_error = ['CARLOS FRANCISCO DE PAULA PROFESSOR', 'JOSE DOS SANTOS PADRE', 'ELISEU NARCISO REVERENDO', 'VITOR MEIRELLES', 'ANIBAL DE FREITAS PROFESSOR', 'UNIVERSIDADE ESTADUAL DE CAMPINAS']

df_educacao = pd.read_parquet('df_educacao_geocode.parquet', engine='pyarrow')
df_educacao = df_educacao.query("nome not in @some_error")
df_educacao['lat'] = df_educacao['geocode'].apply(lambda x: x[0])
df_educacao['lon'] = df_educacao['geocode'].apply(lambda x: x[1])
df_educacao = pd.concat([df_educacao, pd.DataFrame([{'nome' : 'UNIVERSIDADE ESTADUAL DE CAMPINAS', 'geocode': [-22.817220, -47.069440], 'lat' : -22.817220, 'lon' : -47.069440}])], ignore_index=True)

df_geo = df_educacao[['nome', 'lat', 'lon']].copy()
df_geo = pd.concat([df_geo, pd.DataFrame([{'nome' : 'UNIVERSIDADE ESTADUAL DE CAMPINAS', 'lat' : -22.817220, 'lon' : -47.069440}])], ignore_index=True)
df_geo = df_geo.astype({'nome':'str', 'lat':'float64', 'lon':'float64'})

import folium
import streamlit as st

from streamlit_folium import st_folium

campinas = [-22.8957, -47.1078]
APP_TITLE = 'Educação Campinas'
APP_SUB_TITLE = 'Fonte: CENSO/TSE'

def plot_markers(df, m):
    df = df.astype({'desistentes':'int'})
    for _, row in df.iterrows():
        coord = row['geocode']
        name = f"name: {row['nome']}\nvagas: {row['vagas']}\ndesistentes: {row['desistentes']}"
        folium.Marker(coord, popup=name).add_to(m)


def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    
    m = folium.Map(location=campinas, zoom_start=6)
    plot_markers(df_educacao.query("desistentes > 0"), m)
    st_data = st_folium(m, width=400, height=400)

if __name__ == "__main__":
    main()