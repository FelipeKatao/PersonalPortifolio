import pandas as pd 
import pandasql as ps
import DataPySql as dsql

usuarios = pd.read_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\usuarios.csv")
Cargos = pd.read_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\Cargos.csv")

#sqlQUery = dsql.DataPySql.ReadFristQuery("D:\Pessoal\CataoChanel\Tutos\PyData\sql\View_usuarios.sql")
#print(ps.sqldf(sqlQUery,locals()))

query = dsql.DataPySql()
ListQuery = query.ExecAllQuery("D:\Pessoal\CataoChanel\Tutos\PyData\sql\View_usuarios.sql")
for listA in ListQuery:
    print(listA)