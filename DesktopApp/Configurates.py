from xml.dom import minidom
import xml.etree.ElementTree as ET

class Config:
    def __init__(self) -> None:
        ColorClass = []
        pass
    ColorClass = []
    def Readtheme(self):
        tree = ET.parse('./MyBox/Theme.xml')
        root = tree.getroot()
        ThemeDefault = root.attrib
        for child in root.findall("./"+ThemeDefault["name"]+"/ThemeConfig"):
            self.ColorClass.append(child.attrib)
        return self.ColorClass
     
