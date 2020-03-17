import arcade

def bordes():
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

def seccion1():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 5
    BOTTOM_MARGIN = 5
    for row in range(30):
        for column in range(30):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)

def seccion2():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 305
    BOTTOM_MARGIN = 5
    for row in range(30):
        for column in range(30):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.APPLE_GREEN)

def seccion3():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 605
    BOTTOM_MARGIN = 5
    for row in range(30):
        for column in range(30):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.APPLE_GREEN)

def seccion4():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 905
    BOTTOM_MARGIN = 5
    for row in range(30):
        for column in range(30):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.APPLE_GREEN)
                if column % 2 == 0:
                    arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)
                else:
                    arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.APPLE_GREEN)

def seccion5():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 5
    BOTTOM_MARGIN = 305
    for row in range(30):
        for column in range(0 + row, 30):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)

def seccion7():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 315
    BOTTOM_MARGIN = 305
    for row in range(30):
        for column in range(29 , 30 + row):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)

def seccion8():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 905
    BOTTOM_MARGIN = 305
    for row in range(30):
        for column in range(29 - row, 30):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)

def seccion6():
    COLUMN_SPACING = 10
    ROW_SPACING = 10
    LEFT_MARGIN = 305
    BOTTOM_MARGIN = 305
    for row in range(30):
        for column in range(0 , 30-row):
            x = column * COLUMN_SPACING + LEFT_MARGIN
            y = row * ROW_SPACING + BOTTOM_MARGIN
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE_SAPPHIRE)

def main():
    arcade.open_window(1200, 600, "LABORATORIO 5")
    arcade.set_background_color(arcade.color.PURPLE)
    arcade.start_render()

    bordes()
    seccion1()
    seccion2()
    seccion3()
    seccion4()
    seccion5()
    seccion6()
    seccion7()
    seccion8()

    arcade.finish_render()
    arcade.run()

main()