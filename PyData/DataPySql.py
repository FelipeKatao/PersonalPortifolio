
class DataPySql():
    def __init__(self) -> None:
        pass
    def ReadFristQuery(file:str):
        file_query =open(file,"r")
        return file_query.readline()
    
    def ReadQuerySpecific(self,file:str,line:int):
         file_query =open(file,"r")
         return file_query.readlines()[line]

    def ExecAllQuery(self,file:str):
        file_query =open(file,"r")
        Querys= []
        for query in file_query.readlines():
            
            if("UPDATE" in query):
                self.UpdateQuery(query)
            else:
                Querys.append(query)
        return Querys

    def UpdateQuery(self,query):
        query = query.replace("UPDATE","").replace("SET",",").replace("=",",").replace("WHERE",",[")+"]"
        query_list = query.split(',')
        return query_list