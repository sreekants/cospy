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
		""" #TODO: __str__
		"""
		return f'({self.x:.2f}, {self.y:.2f}, {(self.x+self.w):.2f}, {(self.y+self.width):.2f})'

	@property
	def top(self):
		""" #TODO: top
		"""
		return self.y

	@property
	def left(self):
		""" #TODO: left
		"""
		return self.x

	@property
	def bottom(self):
		""" #TODO: bottom
		"""
		return self.y + self.h

	@property
	def right(self):
		""" #TODO: right
		"""
		return self.x + self.w

	@property
	def topleft(self):
		""" #TODO: topleft
		"""
		return self.x, self.y

	@property
	def bottomleft(self):
		""" #TODO: bottomleft
		"""
		return self.x, self.y + self.h

	@property
	def topright(self):
		""" #TODO: topright
		"""
		return self.x + self.w, self.y

	@property
	def bottomright(self):
		""" #TODO: bottomright
		"""
		return self.x + self.w, self.y + self.h

	@property
	def midtop(self):
		""" #TODO: midtop
		"""
		return self.x + self.w / 2, self.y

	@property
	def midleft(self):
		""" #TODO: midleft
		"""
		return self.x, self.y + self.h / 2

	@property
	def midbottom(self):
		""" #TODO: midbottom
		"""
		return self.x + self.w / 2, self.y + self.h

	@property
	def midright(self):
		""" #TODO: midright
		"""
		return self.x + self.w, self.y + self.h / 2

	@property
	def center(self):
		""" #TODO: center
		"""
		return self.x + self.w / 2, self.y + self.h / 2

	@property
	def centerx(self):
		""" #TODO: centerx
		"""
		return self.x + self.w / 2

	@property
	def centery(self):
		""" #TODO: centery
		"""
		return self.y + self.h / 2

	@property
	def size(self):
		""" #TODO: size
		"""
		return self.w, self.h

	@property
	def width(self):
		""" #TODO: width
		"""
		return self.w

	@property
	def height(self):
		""" #TODO: height
		"""
		return self.h


	@top.setter
	def top(self, value):
		""" #TODO: top
		Arguments
			value -- #TODO
		"""
		self.y = value

	@left.setter
	def left(self, value):
		""" #TODO: left
		Arguments
			value -- #TODO
		"""
		self.x = int(value)

	@bottom.setter
	def bottom(self, value):
		""" #TODO: bottom
		Arguments
			value -- #TODO
		"""
		self.y = int(value) - self.h

	@right.setter
	def right(self, value):
		""" #TODO: right
		Arguments
			value -- #TODO
		"""
		self.x = int(value) - self.w

	@topleft.setter
	def topleft(self, value):
		""" #TODO: topleft
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0])
		self.y = int(value[1])

	@bottomleft.setter
	def bottomleft(self, value):
		""" #TODO: bottomleft
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0])
		self.y = int(value[1]) - self.h

	@topright.setter
	def topright(self, value):
		""" #TODO: topright
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0]) - self.w
		self.y = int(value[1])

	@bottomright.setter
	def bottomright(self, value):
		""" #TODO: bottomright
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0]) - self.w
		self.y = int(value[1]) - self.h

	@midtop.setter
	def midtop(self, value):
		""" #TODO: midtop
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0]) - self.w / 2
		self.y = int(value[1])

	@midleft.setter
	def midleft(self, value):
		""" #TODO: midleft
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0])
		self.y = int(value[1]) - self.h / 2

	@midbottom.setter
	def midbottom(self, value):
		""" #TODO: midbottom
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0]) - self.w / 2
		self.y = int(value[1]) - self.h

	@midright.setter
	def midright(self, value):
		""" #TODO: midright
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0]) - self.w
		self.y = int(value[1]) - self.h / 2

	@center.setter
	def center(self, value):
		""" #TODO: center
		Arguments
			value -- #TODO
		"""
		self.x = int(value[0]) - self.w / 2
		self.y = int(value[1]) - self.h / 2

	@centerx.setter
	def centerx(self, value):
		""" #TODO: centerx
		Arguments
			value -- #TODO
		"""
		self.x = int(value) - self.w / 2

	@centery.setter
	def centery(self, value):
		""" #TODO: centery
		Arguments
			value -- #TODO
		"""
		self.y = int(value) - self.h / 2

	@size.setter
	def size(self, value):
		""" #TODO: size
		Arguments
			value -- #TODO
		"""
		if int(value[0]) < 0 or int(value[1]) < 0(self, value):
			self._ensure_proxy()
		self.w, self.h = int(value)

	@width.setter
	def width(self, value):
		""" #TODO: width
		Arguments
			value -- #TODO
		"""
		if int(value) < 0(self, value):
			self._ensure_proxy()
		self.w = int(value)

	@height.setter
	def height(self, value):
		""" #TODO: height
		Arguments
			value -- #TODO
		"""
		if int(value) < 0:
			self._ensure_proxy()
		self.h = int(value)

	def move(self, *pos):
		""" #TODO: move
		Arguments
			*pos -- #TODO
		"""
		x, y = _two_ints_from_args(pos)
		return Rectangle(self.x + x, self.y + y, self.w, self.h)

	def move_ip(self, *pos):
		""" #TODO: move_ip
		Arguments
			*pos -- #TODO
		"""
		x, y = _two_ints_from_args(pos)
		self.x += x
		self.y += y

	def inflate(self, x, y):
		""" #TODO: inflate
		Arguments
			x -- X coordinate
			y -- Y coordinate
		"""
		return Rectangle(self.x - x / 2, self.y - y / 2, self.w + x, self.h + y)

	def inflate_ip(self, x, y):
		""" #TODO: inflate_ip
		Arguments
			x -- X coordinate
			y -- Y coordinate
		"""
		self.x -= x / 2
		self.y -= y / 2
		self.w += x
		self.h += y

	def unionall(self, others):
		""" #TODO: unionall
		Arguments
			others -- #TODO
		"""
		r = Rectangle(self)
		r.unionall_ip(others)
		return r

	def unionall_ip(self, others):
		""" #TODO: unionall_ip
		Arguments
			others -- #TODO
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
		""" #TODO: fit
		Arguments
			other -- #TODO
		"""
		r = Rectangle(self)
		r.fit_ip(*other)
		return r

	def fit_ip(self, other):
		""" #TODO: fit_ip
		Arguments
			other -- #TODO
		"""
		xratio = self.w / float(other.w)
		yratio = self.h / float(other.h)
		maxratio = max(xratio, yratio)
		self.w = int(self.w / maxratio)
		self.h = int(self.h / maxratio)
		self.x = other.x + (other.w - self.w) / 2
		self.y = other.y + (other.h - self.h) / 2

	def normalize(self):
		""" #TODO: normalize
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
			other -- #TODO
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


