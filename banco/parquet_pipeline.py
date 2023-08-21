import pandas as pd
import os

''' from atual schema to parquet '''
patha = os.getcwd()
df_CARGO = pd.read_parquet(os.path.join(patha, 'CARGO.parquet'), engine='pyarrow')
df_ELEICAO = pd.read_parquet(os.path.join(patha, 'ELEICAO.parquet'), engine='pyarrow')
df_MUNICIPIO = pd.read_parquet(os.path.join(patha, 'MUNICIPIO.parquet'), engine='pyarrow')
df_UE = pd.read_parquet(os.path.join(patha, 'UE.parquet'), engine='pyarrow')
dfs_DADOS = []
dfs_VOTAVEL = []
for folderb in [f for f in os.listdir(patha) if (not '.' in f)]:
    print("satrting folder: ", folderb)
    pathb = os.path.join(patha, folderb)
    df_DADOS = pd.read_parquet(os.path.join(pathb, 'DADOS.parquet'), engine='pyarrow')
    dfs_DADOS.append(df_DADOS)
    df_VOTAVEL = pd.read_parquet(os.path.join(pathb, 'VOTAVEL.parquet'), engine='pyarrow')
    dfs_VOTAVEL.append(df_VOTAVEL)

df_DADOS = pd.concat(dfs_DADOS, ignore_index=True)
df_VOTAVEL = pd.concat(dfs_VOTAVEL, ignore_index=True)
