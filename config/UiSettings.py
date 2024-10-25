class UiSettings:
    settings ={}
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
            return settingsString
        else:
            print("Invalid Settings")
            return ""
    def setSetting(self, key, value) -> None:
        try:
            self.settings[key] = value
        except KeyError:
            print(f"'{key}' is not a valid key")
    @staticmethod
    def validateSettings(settings:dict) -> bool:
        #TODO figure out what the json settings are going to be
        if(True):
            return True
        else:
            return False
