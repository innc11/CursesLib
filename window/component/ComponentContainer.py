from abc import ABC


class ComponentContainer(ABC):  # must be inherited by BaseWindow
	def __init__(self):
		self.components = {}

	def addComponent(self, name, component):
		self.components[name] = component
		component.window = self  # must be inherited by BaseWindow

	def removeComponent(self, name):
		del self.components[name]

	def getComponent(self, name):
		return self.components[name]

	def distributeOnInitialize(self):
		for name, component in self.components.items():
			if component.enable:
				component.onWindowInitialize()

	def distributeOnReinitialize(self):
		for name, component in self.components.items():
			if component.enable:
				component.onWindowReinitialize()

	def distributeOnDestroy(self):
		for name, component in self.components.items():
			if component.enable:
				component.onWindowDestroy()

	def distributeOnDraw(self):
		for name, component in self.components.items():
			if component.enable:
				component.onWindowDraw()

	def distributeOnClick(self, x, y):
		for name, component in self.components.items():
			if component.enable:
				component.onWindowClick(x, y)

	def distributeOnUpdate(self, x, y, deltaTime):
		for name, component in self.components.items():
			if component.enable:
				component.onWindowUpdate(x, y, deltaTime)

	def distributeOnMouseWheel(self, x, y, directionUp):
		for name, component in self.components.items():
			if component.enable:
				component.onWindowMouseWheel(x, y, directionUp)

	def __getattr__(self, name):
		if name in self.components:
			return self.components[name]

		raise AttributeError("could not find component or attribute: " + name)

	def __getitem__(self, key):
		if not isinstance(key, str):
			raise TypeError(f"The key must be a string, instead of '{key}' {type(key)}")

		if key in self.components:
			return self.components[key]

		return None
