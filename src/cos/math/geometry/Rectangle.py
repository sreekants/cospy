#!/usr/bin/python
# Filename: Rectangle.py
# Description: Implementation of the Rectangle class


class Rectangle:
	def __init__(self, x, y, width, height):
		""" Constructor
		Arguments
			x -- X coordinate
			y -- Y coordinate
			width -- #TODO
			height -- #TODO
		"""
		self.x		= x
		self.y		= y
		self.h		= height
		self.w		= width
		return

	def __str__(self):
		""" Returns the string representation of the rectangle
		"""
		return f'({self.x:.2f}, {self.y:.2f}, {(self.x+self.w):.2f}, {(self.y+self.width):.2f})'

	@property
	def top(self):
		""" Returns the top coordinate of the rectangle
		"""
		return self.y

	@property
	def left(self):
		""" Returns the left coordinate of the rectangle
		"""
		return self.x

	@property
	def bottom(self):
		""" Returns the bottom coordinate of the rectangle
		"""
		return self.y + self.h

	@property
	def right(self):
		""" Returns the right coordinate of the rectangle
		"""
		return self.x + self.w

	@property
	def topleft(self):
		""" Returns the top-left coordinate of the rectangle
		"""
		return self.x, self.y

	@property
	def bottomleft(self):
		""" Returns the bottom-left coordinate of the rectangle
		"""
		return self.x, self.y + self.h

	@property
	def topright(self):
		""" Returns the top-right coordinate of the rectangle
		"""
		return self.x + self.w, self.y

	@property
	def bottomright(self):
		""" Returns the bottom-right coordinate of the rectangle
		"""
		return self.x + self.w, self.y + self.h

	@property
	def midtop(self):
		""" Returns the mid-top coordinate of the rectangle
		"""
		return self.x + self.w / 2, self.y

	@property
	def midleft(self):
		""" Returns the mid-left coordinate of the rectangle
		"""
		return self.x, self.y + self.h / 2

	@property
	def midbottom(self):
		""" Returns the mid-bottom coordinate of the rectangle
		"""
		return self.x + self.w / 2, self.y + self.h

	@property
	def midright(self):
		""" Returns the mid-right coordinate of the rectangle
		"""
		return self.x + self.w, self.y + self.h / 2

	@property
	def center(self):
		""" Returns the center coordinate of the rectangle
		"""
		return self.x + self.w / 2, self.y + self.h / 2

	@property
	def centerx(self):
		""" Returns the x-coordinate of the center of the rectangle
		"""
		return self.x + self.w / 2

	@property
	def centery(self):
		""" Returns the y-coordinate of the center of the rectangle
		"""
		return self.y + self.h / 2

	@property
	def size(self):
		""" Returns the size of the rectangle as a tuple (width, height)
		"""
		return self.w, self.h

	@property
	def width(self):
		""" Returns the width of the rectangle
		"""
		return self.w

	@property
	def height(self):
		""" Returns the height of the rectangle
		"""
		return self.h


	@top.setter
	def top(self, value):
		""" Sets the top coordinate of the rectangle
		Arguments
			value -- The new top coordinate
		"""
		self.y = value

	@left.setter
	def left(self, value):
		""" Sets the left coordinate of the rectangle
		Arguments
			value -- The new left coordinate
		"""
		self.x = int(value)

	@bottom.setter
	def bottom(self, value):
		""" Sets the bottom coordinate of the rectangle
		Arguments
			value -- The new bottom coordinate
		"""
		self.y = int(value) - self.h

	@right.setter
	def right(self, value):
		""" Sets the right coordinate of the rectangle
		Arguments
			value -- The new right coordinate
		"""
		self.x = int(value) - self.w

	@topleft.setter
	def topleft(self, value):
		""" Sets the top-left coordinate of the rectangle
		Arguments
			value -- The new top-left coordinate
		"""
		self.x = int(value[0])
		self.y = int(value[1])

	@bottomleft.setter
	def bottomleft(self, value):
		""" Sets the bottom-left coordinate of the rectangle
		Arguments
			value -- The new bottom-left coordinate
		"""
		self.x = int(value[0])
		self.y = int(value[1]) - self.h

	@topright.setter
	def topright(self, value):
		""" Sets the top-right coordinate of the rectangle
		Arguments
			value -- The new top-right coordinate
		"""
		self.x = int(value[0]) - self.w
		self.y = int(value[1])

	@bottomright.setter
	def bottomright(self, value):
		""" Sets the bottom-right coordinate of the rectangle
		Arguments
			value -- The new bottom-right coordinate
		"""
		self.x = int(value[0]) - self.w
		self.y = int(value[1]) - self.h

	@midtop.setter
	def midtop(self, value):
		""" Sets the mid-top coordinate of the rectangle
		Arguments
			value -- The new mid-top coordinate
		"""
		self.x = int(value[0]) - self.w / 2
		self.y = int(value[1])

	@midleft.setter
	def midleft(self, value):
		""" Sets the mid-left coordinate of the rectangle
		Arguments
			value -- The new mid-left coordinate
		"""
		self.x = int(value[0])
		self.y = int(value[1]) - self.h / 2

	@midbottom.setter
	def midbottom(self, value):
		""" Sets the mid-bottom coordinate of the rectangle
		Arguments
			value -- The new mid-bottom coordinate
		"""
		self.x = int(value[0]) - self.w / 2
		self.y = int(value[1]) - self.h

	@midright.setter
	def midright(self, value):
		""" Sets the mid-right coordinate of the rectangle
		Arguments
			value -- The new mid-right coordinate
		"""
		self.x = int(value[0]) - self.w
		self.y = int(value[1]) - self.h / 2

	@center.setter
	def center(self, value):
		""" Sets the center coordinate of the rectangle
		Arguments
			value -- The new center coordinate
		"""
		self.x = int(value[0]) - self.w / 2
		self.y = int(value[1]) - self.h / 2

	@centerx.setter
	def centerx(self, value):
		""" Sets the x-coordinate of the center of the rectangle
		Arguments
			value -- The new x-coordinate of the center
		"""
		self.x = int(value) - self.w / 2

	@centery.setter
	def centery(self, value):
		""" Sets the y-coordinate of the center of the rectangle
		Arguments
			value -- The new y-coordinate of the center
		"""
		self.y = int(value) - self.h / 2

	@size.setter
	def size(self, value):
		""" Sets the size of the rectangle
		Arguments
			value -- The new size as a tuple (width, height)
		"""
		if int(value[0]) < 0 or int(value[1]) < 0(self, value):
			self._ensure_proxy()
		self.w, self.h = int(value)

	@width.setter
	def width(self, value):
		""" Sets the width of the rectangle
		Arguments
			value -- The new width
		"""
		if int(value) < 0(self, value):
			self._ensure_proxy()
		self.w = int(value)

	@height.setter
	def height(self, value):
		""" Sets the height of the rectangle
		Arguments
			value -- The new height
		"""
		if int(value) < 0:
			self._ensure_proxy()
		self.h = int(value)

	def move(self, *pos):
		""" Moves the rectangle by a given offset
		Arguments
			*pos -- The offset as a tuple (x, y) or two separate values
		"""
		x, y = _two_ints_from_args(pos)
		return Rectangle(self.x + x, self.y + y, self.w, self.h)

	def move_ip(self, *pos):
		""" Moves the rectangle in place by a given offset
		Arguments
			*pos -- The offset as a tuple (x, y) or two separate values
		"""
		x, y = _two_ints_from_args(pos)
		self.x += x
		self.y += y

	def inflate(self, x, y):
		""" Returns a new rectangle inflated by the given amounts
		Arguments
			x -- The amount to inflate horizontally
			y -- The amount to inflate vertically
		"""
		return Rectangle(self.x - x / 2, self.y - y / 2, self.w + x, self.h + y)

	def inflate_ip(self, x, y):
		""" Inflates the rectangle in place by the given amounts
		Arguments
			x -- The amount to inflate horizontally
			y -- The amount to inflate vertically
		"""
		self.x -= x / 2
		self.y -= y / 2
		self.w += x
		self.h += y

	def unionall(self, others):
		""" Returns a new rectangle that encloses all given rectangles
		Arguments
			others -- An iterable of rectangles to enclose
		"""
		r = Rectangle(self)
		r.unionall_ip(others)
		return r

	def unionall_ip(self, others):
		""" Updates the rectangle to enclose all given rectangles
		Arguments
			others -- An iterable of rectangles to enclose
		"""
		l = self.x
		r = self.x + self.w
		t = self.y
		b = self.y + self.h
		for other in others:
			l = min(l, other.x)
			r = max(r, other.x + other.w)
			t = min(t, other.y)
			b = max(b, other.y + other.h)
		self.x, self.y, self.w, self.h = l, t, r - l, b - t

	def fit(self, other):
		""" Returns a new rectangle that fits within another rectangle
		Arguments
			other -- The rectangle to fit within
		"""
		r = Rectangle(self)
		r.fit_ip(*other)
		return r

	def fit_ip(self, other):
		""" Adjusts the rectangle to fit within another rectangle in place
		Arguments
			other -- The rectangle to fit within
		"""
		xratio = self.w / float(other.w)
		yratio = self.h / float(other.h)
		maxratio = max(xratio, yratio)
		self.w = int(self.w / maxratio)
		self.h = int(self.h / maxratio)
		self.x = other.x + (other.w - self.w) / 2
		self.y = other.y + (other.h - self.h) / 2

	def normalize(self):
		""" Normalizes the rectangle's dimensions
		"""
		if self.w < 0:
			self.x += self.w
			self.w = -self.w
		if self.h < 0:
			self.y += self.h
			self.h = -self.h

	def contains(self, other):
		""" Checks if a rectangle is enclosed by another
		Arguments
			other -- The rectangle to check
		"""
		return self.x <= other.x and \
				self.y <= other.y and \
				self.x + self.w >= other.x + other.w and \
				self.y + self.h >= other.y + other.h and \
				self.x + self.w > other.x and \
				self.y + self.h > other.y


	def encloses(self, x, y):
		""" Checks if a point is enclosed by the rectange
		Arguments
			x -- X coordinate
			y -- Y coordinate
		"""
		return x >= self.x and \
				y >= self.y and \
				x < self.x + self.w and \
				y < self.y + self.h

def _two_ints_from_args(arg):
    """ #TODO: _two_ints_from_args
    Arguments
    	arg -- #TODO
    """
    if len(arg) == 1:
        return _two_ints_from_args(arg[0])
    else:
        return arg[:2]

if __name__ == "__main__":
	test = Rectangle()


