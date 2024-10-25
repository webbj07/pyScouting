import config.UiSettings as UiSettings
class UiElement:
    data = 0
    settings: UiSettings.UiSettings = None
    def __init__(self, settings:UiSettings.UiSettings, numericalStartingData) -> None:
        self.settings = settings
        self.data = numericalStartingData
    def getData(self): return self.data
    def setData(self, data) -> None: self.data = data
    def setSettings(self, settings:UiSettings.UiSettings):
        self.settings =settings
    def getSettings(self) -> UiSettings.UiSettings:
        return self.settings
