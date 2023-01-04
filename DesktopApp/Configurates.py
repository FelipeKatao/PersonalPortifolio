from xml.dom import minidom
import xml.etree.ElementTree as ET

class Config:
    def __init__(self) -> None:
        ColorClass = []
        pass
    ColorClass = []
    ThemeClass = []
    def Readtheme(self):
        tree = ET.parse('./MyBox/Theme.xml')
        root = tree.getroot()
        ThemeDefault = root.attrib
        for child in root.findall("./"+ThemeDefault["name"]+"/ThemeConfig"):
            self.ColorClass.append(child.attrib)
        return self.ColorClass
     
    def ReadThemesInSystem(self):
        tree = ET.parse('./MyBox/Theme.xml')
        root = tree.getroot()
        for child in root:
            self.ThemeClass.append(child.tag)
        pass

    def ModifyTheme(self,Theme):
        tree = ET.parse('./MyBox/Theme.xml')
        root = tree.getroot()
        ThemeDefault = root.attrib
        print(ThemeDefault)
        ThemeDefault["name"] = Theme
        tree.write('./MyBox/Theme.xml')
        pass

