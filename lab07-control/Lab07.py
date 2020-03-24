import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
SPRITE_SCALING = 0.5

class PacMan(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):

    def  __init__(self, width, height):

        super().__init__(width, height)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.PacMan_sprite = None
        self.PacMan_list = None
        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        self.PacMan_list = arcade.SpriteList()
        self.PacMan_sprite = PacMan(":resources:images/practicas/pacman.png", SPRITE_SCALING)
        self.PacMan_sprite.center_x = 50
        self.PacMan_sprite.center_y = 50
        self.PacMan_list.append(self.PacMan_sprite)

    def on_draw(self):
        arcade.start_render()
        self.PacMan_list.draw()

    def on_update(self, delta_time):
        self.PacMan_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.PacMan_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.PacMan_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.PacMan_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.PacMan_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.PacMan_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.PacMan_sprite.change_x = 0

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()