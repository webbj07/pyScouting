import UiElement
class UiCounter(UiElement):
    # local varables:
    # type of Tk ui element
    # positive and negative clicking buttons
    # display data for that ui element
    count:int = 0
    text:str = ""
    def __init__(self):
        pass
    def __init__(self, startingValue, text):
        self.count = startingValue
        self.text = text
    def display(self):
        """display the counter onscreen"""
        #TODO display the counter
        pass
    def handlePositiveClick(self):
        self.data += 1
    def handleNegativeClick(self):
        self.data -= 1
