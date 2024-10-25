import UiElement
class UiText(UiElement):
    text:str = ""
    xPos:int = 0
    yPos:int = 0

    def __init__(self, text, xPos, yPos) -> None:
        self.text = text
        self.xPos = xPos
        self.yPos = yPos
    def display(self):
        #TODO display text onto screen
        pass
