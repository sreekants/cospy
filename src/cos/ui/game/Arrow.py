#!/usr/bin/python
# Filename: Arrow.py
# Description: Renders an arrow
# Source: https://www.reddit.com/r/pygame/comments/v3ofs9/draw_arrow_function/

import pygame



class Arrow:
	def __init__(self, start:pygame.Vector2, end:pygame.Vector2, width:int = 1, head_width:int = 6, head_height:int = 8, color: pygame.Color=(255,0,0) ):
		""" Creates an arrow between start and end with the arrow head at the end.
		Args:
			start (pygame.Vector2): Start position
			end (pygame.Vector2): End position
			color (pygame.Color): Color of the arrow
			body_width (int, optional): Defaults to 2.
			head_width (int, optional): Defaults to 4.
			head_height (float, optional): Defaults to 2.
		"""
		self.color	= color
		self.start	= start
		self.end	= end
		self.width	= width
		self.head	= (head_width, head_height)
		self.layer	= 1
		self.compose()
		return

	def compose(self):
		""" Calculate the shape of the arrow.
		"""
		head_width	= self.head[0]
		head_height	= self.head[1]
		arrow 		= self.start - self.end
		angle 		= arrow.angle_to(pygame.Vector2(0, -1))

		# Create the triangle head around the origin
		self.arrowhead = [
			pygame.Vector2(0, head_height / 2),  # Center
			pygame.Vector2(head_width / 2, -head_height / 2),  # Bottomright
			pygame.Vector2(-head_width / 2, -head_height / 2),  # Bottomleft
		]

		# Rotate and translate the head into place
		translation = pygame.Vector2(0, arrow.length() - (head_height / 2)).rotate(-angle)
		for h in self.arrowhead:
			h.rotate_ip(-angle)
			h += translation
			h += self.start

		return

	def render(self, ctxt, screen):
		""" Renders the arrow
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if ctxt.layer != self.layer:
			return

		head_height	= self.head[1]
		arrow 		= self.start - self.end
		body_length = arrow.length() - abs(head_height)

		pygame.draw.polygon(screen, self.color, ctxt.encoder.transform_polygon(self.arrowhead) )

		# Stop weird shapes when the arrow is shorter than arrow head
		if body_length >= 0:
			angle 		= arrow.angle_to(pygame.Vector2(0, -1))

			# Calculate the body rect, rotate and translate into place
			body = [
				pygame.Vector2(-self.width / 2, body_length / 2),  # Topleft
				pygame.Vector2(self.width / 2, body_length / 2),  # Topright
				pygame.Vector2(self.width / 2, -body_length / 2),  # Bottomright
				pygame.Vector2(-self.width / 2, -body_length / 2),  # Bottomleft
			]
			translation = pygame.Vector2(0, body_length / 2).rotate(-angle)
			for i in range(len(body)):
				body[i].rotate_ip(-angle)
				body[i] += translation
				body[i] += self.start

			pygame.draw.polygon(screen, self.color, ctxt.encoder.transform_polygon(body) )

if __name__ == "__main__":
	pygame.init()

	CLOCK = pygame.time.Clock()
	FPS = 60

	WIDTH = 1280
	HEIGHT = 720
	RESOLUTION = (WIDTH, HEIGHT)
	SCREEN = pygame.display.set_mode(RESOLUTION)

	while True:
		CLOCK.tick(FPS)

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

		SCREEN.fill(pygame.Color("black"))

		center = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
		end = pygame.Vector2(pygame.mouse.get_pos())
		arrow = Arrow(center, end, 1, 6, 8, pygame.Color("red"))
		arrow.render(None, SCREEN)

		pygame.display.flip()


