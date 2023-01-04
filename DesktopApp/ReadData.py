from xml.dom import minidom
import xml.etree.ElementTree as ET

class ReadDataBase:
    def __init__(self) -> None:
        pass
    def ReturnData():
        file = minidom.parse("./MyBox/UserBase.xml")
        tagGet = file.getElementsByTagName('Database')
        return [tagGet[0].firstChild.data,tagGet[0].attributes['name'].value]
        
        
    def ReadData():
        file = "./MyBox/UserBase.xml"
        tagGet = ET.parse(file)
        rootElement = tagGet.getroot()
        for element in rootElement.findall("NomeBase"):
           element.find("Database").text = "<h3>TESTE</h3>"
        tagGet.write(file,encoding='UTF-8',xml_declaration=True)