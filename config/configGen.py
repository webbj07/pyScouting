from typing import List, Type
import UiSettings
class ConfigGen:
    """Class to generate config files given user string input"""
    Json:str = "{"
    def __init__(self, initalJson) -> None:
        self.Json = initalJson
    def __init__(self) -> None:
        pass
    def addElement(self, objectName:str, settings:List[Type[UiSettings]]):
        stringToAdd = ""
        stringToAdd += f"{objectName} ["
