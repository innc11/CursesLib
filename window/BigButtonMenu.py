import curses
from abc import ABC

from window.BaseWindow import BaseWindow
from window.component.ScrollBar import ScrollBar


class BigButtonMenu(BaseWindow, ABC):
	def __init__(self, monopolyMode=False, maskMode=False):
		super().__init__(monopolyMode, maskMode)

		self.buttons = []
		self.itemHeight = 3  # 每个按钮的高度
		self.yOffset = 0  # 按钮向下的偏移量，方便在窗口最上方留点位置去绘制其它的东西

		self.addComponent("sb", ScrollBar())

	def onDraw(self):
		self.drawBorder()
		self.drawButton()

	def drawButton(self):

		for i in range(0, len(self.buttons)):
			b = self.buttons[i]

			self.randomColor()

			dh = self.itemHeight + 1

			string = f"{{:^{self.width - 3}}}".format(b[0])
			self.screen.addstr(self.yOffset + 2 + (i * dh), 1, string)

			if i != 0:
				self.screen.addstr(self.yOffset + 0 + (i * dh), 1, f"{{:^{self.width - 3}}}".format("------------------------"))

			self.resetColor()

	def add(self, text, callback, *args):
		self.buttons.append([text, callback, *args])
		self.drawAFrame()

	def onClick(self, x, y):
		ch = self.itemHeight

		for i in range(0, len(self.buttons)):
			start = i * (ch + 1) + 1 + self.yOffset
			end = start + 2

			if start <= y <= end:
				self.doClick(i)
				curses.flash()

	def doClick(self, index):

		item = self.buttons[index]

		if item[1] is not None:
			item[1](self, item)
			self.drawAFrame()

	def doClickByText(self, text):
		for item in self.buttons:
			if item[0] == text:
				if item[1] is not None:
					if item[1](self, item):
						self.drawAFrame()
					return True
		return False

	def __repr__(self):
		return "BigButtonMenu"
