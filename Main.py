from Terminal import Terminal
from window.BigButtonMenu import BigButtonMenu
from window.component.CloseButton import CloseButton
from window.component.WindowTitle import WindowTitle


class MainMenu(BigButtonMenu):
    def __init__(self, monopolyMode, maskMode):
        super().__init__(monopolyMode, maskMode)

        self.elapsedTime = 0

        self.addComponent("title", WindowTitle("Main Test Menu"))
        self.addComponent("close", CloseButton())

        self.add("Run Test", lambda win, item: win.execute(
            lambda: print("Hello World"), 3000
        ))

        self.add("Quit Test", lambda win, item: win.release())

    def onUpdate(self, x, y, deltaTime):
        self.elapsedTime += deltaTime

        if self.elapsedTime > 1000:
            self.elapsedTime = 0
            # print("aaaaa")


if __name__ == "__main__":

    ts = Terminal()

    ts.addAWindow(MainMenu(monopolyMode=True, maskMode=True))

    ts.mainLoop()
