import pandas as pd 
import pandasql as ps
import DataPySql as dsql

usuarios = pd.read_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\usuarios.csv")
Cargos = pd.read_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\Cargos.csv")

#sqlQUery = dsql.DataPySql.ReadFristQuery("D:\Pessoal\CataoChanel\Tutos\PyData\sql\View_usuarios.sql")
#print(ps.sqldf(sqlQUery,locals()))

SqlQuery = dsql.DataPySql()
SqlQuery.ExecAllQuery("PyData\sql\View_usuarios.sql",0)
print(SqlQuery.ReadQuerySpecific("PyData\sql\View_usuarios.sql",2))

