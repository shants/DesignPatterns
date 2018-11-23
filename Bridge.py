from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class DrawImpl():
	__metaclass__ = ABCMeta
	@abstractmethod
	def draw_circle(cls, x,y,radius):
		raise NotImplemented(NOT_IMPLEMENTED)


class DrawImpl1(DrawImpl):
	def draw_circle(self, x, y, radius):
		print("API1.circle at {0}:{1} - radius: {2}".format(x, y, radius))

class DrawImpl2(DrawImpl):
	def draw_circle(self, x, y, radius):
		print("API2.circle at {0}:{1} - radius: {2}".format(x, y, radius))

class Shape():
	__metaclass__ = ABCMeta

	drawing_api = None
	def __init__(self, drawing_impl):
		self.drawing_impl = drawing_impl

	@abstractmethod
	def draw(cls):
		raise NotImplemented(NOT_IMPLEMENTED)


class CircleShape(Shape):
	def __init__(self,x,y,radius, drawing_impl):
		self.x = x
		self.y = y
		self.radius = radius
		super().__init__(drawing_impl)

	def draw(cls):
		cls.drawing_api.draw_circle(cls.x, cls.y, cls.radius)


if __name__ == "__main__":
	d1 = DrawImpl1()
	d2 = DrawImpl2()
	c = CircleShape(1,2,5,d2)
	(c.draw())

