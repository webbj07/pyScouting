class UiElement:
    data = 0
    name = ""
    id = 0
    def __init__(self, name, numericalStartingData, id) -> None:
        self.name = name
        self.data = numericalStartingData
        self.id = id
    def getData(self): return self.data
    def getId(self): return self.id
    def getName(self): return self.data

    def setData(self, data) -> None: self.data = data
    def setname(self, name) -> None: self.name = name
    def setId(self, id) -> None: self.id = id
