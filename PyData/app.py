import pandas as pd 
import pandasql as ps
import DataPySql as dsql

usuarios = pd.read_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\usuarios.csv")
Cargos = pd.read_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\Cargos.csv")

#sqlQUery = dsql.DataPySql.ReadFristQuery("D:\Pessoal\CataoChanel\Tutos\PyData\sql\View_usuarios.sql")
#print(ps.sqldf(sqlQUery,locals()))

# Localizar os Usuarios apenas
usuarios = pd.read_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\usuarios.csv")
df = pd.DataFrame(usuarios)
#df.index=[df.Usario]
df.index=[0,0,0,0,0,0]
# ou  print(df.loc["Lucas"])
df.loc[0,"Acessos"] = 1
print(df)
df.to_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\usuarios.csv",index=False)

