#!/usr/bin/python
# Filename: VehicleSprite.py
# Description: Implementation of mobile vehicle sprites.

from cos.ui.game.Sprite import Sprite

from cos.ui.game.Config import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

class VehicleSprite(Sprite):
    def __init__(self ,config):
        """ Constructor
        Arguments
        	config -- Configuration attributes
        """
        super(VehicleSprite, self).__init__(
            config,
            "img/cos.png",
            (255, 255, 255) )

        self.rect = self.surf.get_rect( center=(120, 120) )
        return

    # Move the sprite based on keypresses
    def update(self, world, pressed_keys):
        """ Updates the sprite location with the key pressed
        Arguments
        	world -- Reference ot the simulation world
        	pressed_keys -- Map of the keys pressed.
        """
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            # move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            # move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH-10:
            self.rect.right = SCREEN_WIDTH-10
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT-10:
            self.rect.bottom = SCREEN_HEIGHT-10




if __name__ == "__main__":
	test = VehicleSprite()


