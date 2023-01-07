
class DataPySql():
    def __init__(self) -> None:
        pass
    def ReadFristQuery(file:str):
        file_query =open(file,"r")
        return file_query.readline()
    
    def ReadQuerySpecific(self,file:str,line:int):
         file_query =open(file,"r")
         return file_query.readlines()[line]

    def ExecAllQuery(self,file:str,function):
        file_query =open(file,"r")
        for query in file_query.readlines():
            print(query)