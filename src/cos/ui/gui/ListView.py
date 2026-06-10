#!/usr/bin/python
# Filename: ListView.py
# Description: Implementation of the ListView class

import cos.ui.gui.Style as Style

import pygame

class ListView:
	def __init__(self, title, pos):
		self.title		= title
		self.pos		= pos
		self.items		= []
		return

	def clear(self):
		self.items.clear()
		return

	def append(self, txt, pos=None, size=None, color=None):
		self.items.append( (pos, size, txt, color) )
		return

	def render(self, ctxt, parent):
		self.render_title(ctxt, parent)
		self.render_items(ctxt, parent)
		return

	def render_title(self, ctxt, parent):
		title_pos		= 15
		line_offset		= 20

		# Title Text
		nexty			= self.pos[1]+title_pos
		title_surface 	= parent.font_title.render( self.title, True, Style.TEXT_PRIMARY)
		ctxt.screen.blit( title_surface, (parent.box_rect.left + parent.margin, parent.box_rect.top+nexty) )

		# Header / Accent Line inside the box
		nexty			= nexty+line_offset
		pygame.draw.line(
			ctxt.screen,
			Style.ACCENT_FOCUS,
			(parent.box_rect.left + parent.margin, parent.box_rect.top+nexty),
			(parent.box_rect.right - parent.margin, parent.box_rect.top+nexty),
			width=1,
		)


		# Reset the pos
		self.viewpos	= (self.pos[0], nexty)
		return

	def render_items(self, ctxt, parent):	
		for idx, l in enumerate(self.items):
			loc		= l[0]
			size	= l[1]
			txt		= l[2]

			# Render the text
			at		= (0, self.viewpos[1]+15*idx) if loc is None else loc
			
			parent.text(ctxt, parent.font_body, at, txt, l[3])
		
		return

if __name__ == "__main__":
	test = ListView()

