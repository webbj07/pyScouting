import ui.UiElement as UiElement
class configUtil:

    elements = []
    def __init__(self, elements:list[UiElement.UiElement]) -> None:
        self.elements = elements
    def __init__(self) -> None:
        pass
    @staticmethod
    def createConfigFromElements(elements:list[UiElement.UiElement]) -> str:
        """Writes a json config file"""
        toWrite = "{"
        for element in elements:
            settings = element.getSettings()
            toWrite += f"{settings["name"]}:["
            for setting in settings:
                toWrite += f"{setting} : {settings[setting]},\n"
            toWrite += "],\n"
        toWrite += "}"
        return toWrite
    @staticmethod
    def CreateElementsFromConfig(json:str) -> None:
