import pandas as pd 
import pandasql as ps
import csv



DataBase = R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\usuarios.csv"

#INSERT
dataAppend = {
    'Usuario':['Felipe'],
    'IdUsuario':[12],
    'Acessos':[1],
    'Modulo':['PAGAMENTO']
}
df = pd.DataFrame(dataAppend)
df.to_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\usuarios.csv",mode='a',index=False,header=False)
 

#UPDATE 

df = pd.read_csv(DataBase)
Data_Update = pd.DataFrame(df)
df.loc[Data_Update[Data_Update.Usuario == "Joao"],'Acessos'] = 6
df.to_csv(DataBase,index=False)


#DELETE 

df = pd.read_csv(DataBase)
df.index=["one","two","three","four","five","six"]
DataFrame_ = pd.DataFrame(df)
df = DataFrame_.drop(DataFrame_[DataFrame_.Usuario == "Joao"].index)
df.to_csv(DataBase,index=False)
print(df)


#ITERAR A TABELA 
print('====================================')
usuarios = pd.read_csv(R"D:\Pessoal\CataoChanel\Tutos\PyData\DataBase\usuarios.csv")
for value,item in usuarios.iterrows():
    print(item["Usuario"])