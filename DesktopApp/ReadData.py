from xml.dom import minidom
import xml.etree.ElementTree as ET

class ReadDataBase:
    def __init__(self) -> None:
        pass
    ElementsNode = ["titulo","subtitulo","tasks"]
    BodyElement = {}
    TasksElements = []
    def ReturnData(self):
        tree = ET.parse('./MyBox/UserBase.xml')
        root = tree.getroot()
        for Elem in self.ElementsNode:
            for child in root.findall("./nootbook[@name='inicial']/"+Elem):
                if Elem == "tasks":
                    self.TasksElements.append(child.text)
                else:
                    self.BodyElement[Elem] = child.text
        print(self.TasksElements)
        return self.BodyElement
        
    def GetTasks(self):
        return self.TasksElements  
    def ReadData():
        return 0