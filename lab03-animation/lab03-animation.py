import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_sky():
    arcade.set_background_color(arcade.csscolor.AQUA)

def draw_ground():
    arcade.draw_lrtb_rectangle_filled(0, 599, 150, 0, arcade.csscolor.GREEN)

def draw_tree():
    arcade.draw_lrtb_rectangle_filled(200, 275, 400, 150, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(300, 400, 100, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(200, 400, 100, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(250, 500, 100, arcade.csscolor.DARK_GREEN)

def draw_fruit1(y):
    arcade.draw_ellipse_filled(350, y, 30, 40, arcade.csscolor.DARK_BLUE)
    arcade.draw_rectangle_filled(350, y+20, 5, 10, arcade.csscolor.SIENNA)

def draw_fruit2(y):
    arcade.draw_circle_filled(160, y , 20, arcade.csscolor.ORANGE)

def draw_bird():
    arcade.draw_ellipse_filled(250, 500, 80, 30, arcade.csscolor.BURLYWOOD)
    arcade.draw_rectangle_filled(250, 510, 10, 20, arcade.csscolor.BLUE_VIOLET)
    arcade.draw_arc_filled(233, 500, 30, 70, arcade.csscolor.BLACK, 0, 40)
    arcade.draw_arc_filled(243, 500, 30, 70, arcade.csscolor.BLACK, 0, 40)
    arcade.draw_circle_filled(250, 527, 10, arcade.csscolor.BLUE_VIOLET)
    arcade.draw_circle_filled(255, 529, 2, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(261, 523, 7, 3, arcade.csscolor.BLACK)

def draw_sun(x):
    arcade.draw_circle_filled(x, 590, 150, arcade.csscolor.YELLOW)

def draw_camp():
    arcade.draw_triangle_filled(450, 350, 600, 150, 300, 150, arcade.csscolor.RED)
    arcade.draw_lrtb_rectangle_filled(447, 452, 360, 150, arcade.csscolor.BROWN)

def on_draw(delta_time):
    arcade.start_render()
    draw_sky()
    draw_ground()
    draw_tree()
    draw_fruit1(on_draw.fruit1)
    on_draw.fruit1 -= 1
    draw_fruit2(on_draw.fruit2)
    on_draw.fruit2 -= 1
    draw_bird()
    draw_sun(on_draw.sun)
    on_draw.sun += 1
    draw_camp()

on_draw.fruit2=400
on_draw.fruit1=350
on_draw.sun = 570

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "CAMPING")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()
