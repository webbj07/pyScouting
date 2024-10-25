class UiSettings:

    settings = {
        "type": "",
        "title": "",
        "name": "",
        "id": "",
        "xPos": 0,
        "yPos": 0
    }

    def __init__(self) -> None:
        pass

    def __init__(self, settings:dict) -> None:
        if(UiSettings.validateSettings(settings)):
            self.settings = settings
        else:
            print("invalid inital settings for constructor")
    def getSettings(self) -> dict: return self.settings

    def getSettingsString(self) -> str:
        if UiSettings.validateSettings(self.settings):
            settingsString = ""
            count = 0
            for key in self.settings:
                settingsString += f"{key}: {self.settings[key]},\n"
            return settingsString + "}"
        else:
            print("Invalid Settings")
            return ""
    def setSetting(self, key:str, value) -> None:
        try:
            self.settings[key.lower()] = value
        except KeyError:
            print(f"'{key}' is not a valid key")

    @staticmethod
    def validateSettings(settings:dict) -> bool:
        #TODO figure out what the json settings are going to be
        if(True):
            pass
        else:
            return False
