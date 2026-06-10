#!/usr/bin/python
# Filename: Infobox.py
# Description: Implementation of the Infobox class

from cos.ui.gui.ListView import ListView
import cos.ui.gui.Style as Style

import pygame


class Infobox:
	def __init__(self):
		self.labels		= []	# Log text to overlay over the map
		self.children	= []
		self.relative	= False
		return

	def init(self):
		self.font_title		= pygame.font.SysFont("helvetica", 16, bold=True)
		self.font_body		= pygame.font.SysFont("helvetica", 14)
		self.font_small		= pygame.font.SysFont("helvetica", 10)
		self.box_rect 		= pygame.Rect(950, 10, 200, 400)
		self.margin			= 20
		self.pos			= (self.box_rect.left + self.margin, self.box_rect.top+15)

		# Add child views
		self.zones			= ListView('Zones', (0,0))
		self.objects		= ListView('Objects', (0,150))

		self.children.extend( [self.zones, self.objects] )

		self.show( False )
		return

	def show(self, istrue):
		for c in self.children:
			c.show(istrue)
		self.visible		= istrue
		return

	def append_object(self, z:str):
		self.objects.append(z)
		return


	def append_sea(self, z:str):
		self.zones.append(z)
		return
	
	def append_land(self, z:str):
		self.zones.append(z)
		return
	
	def append_sky(self, z:str):
		self.zones.append(z)
		return

	def append_zone(self, z:str):
		self.zones.append(z)
		return
	

	def clear(self):
		self.zones.clear()
		self.objects.clear()
		return

	def render(self, ctxt):
		if not self.visible:
			return
		
		self.__render_mouse(ctxt)
		self.__render_box(ctxt)

		for w in self.children:
			w.render( ctxt, self)
			
		return

	
	def at(self, x, y):
		return (self.box_rect.left + x, self.box_rect.top + y)

	def text(self, ctxt, font, pos, txt, color=None):
		# Position text relative to the window
		self.text_at( ctxt, font, (self.pos[0]+pos[0],self.pos[1]+pos[1]), txt, color )
		return

	def text_at(self, ctxt, font, pos, txt, color=None):
		color		= color if color else Style.TEXT_MUTED
		text		= self.font_body.render( txt, False, color)

		ctxt.screen.blit( text, pos)
		return

	def __render_box(self, ctxt):
		# Elevated Layer (The Off-Black Box)
		# Draw a subtle drop shadow using a slightly offset transparent/darker surface
		shadow_rect 			= self.box_rect.move(4, 4)

		pygame.draw.rect(ctxt.screen, Style.BOX_SHADOW, shadow_rect)

		# Main Box Surface
		pygame.draw.rect(ctxt.screen, Style.BOX_COLOR, self.box_rect)
		
		# Thin, elegant border edge
		pygame.draw.rect(ctxt.screen, Style.BORDER_COLOR, self.box_rect, width=1)
		return



	def __render_mouse(self, ctxt):
		cursor 		= pygame.mouse.get_pos()
		if self.relative:
			pos			= (cursor[0]-self.box_rect.left, cursor[1]-self.box_rect.top)
		else:
			pos			= (cursor[0], cursor[1])

		text		= self.font_body.render( f'cursor:{cursor[0]-self.box_rect.left},{cursor[1]-self.box_rect.top}', False, (0,0,0))
		ctxt.screen.blit( text, pos)
		return

		

if __name__ == "__main__":
	test = Infobox()

