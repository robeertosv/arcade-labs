import arcade

arcade.open_window(600, 600, "EPS LOGO")
arcade.set_background_color(arcade.color.WHITE)
EPS = (162, 84,28)
arcade.start_render()

#Cuadrados EPS
arcade.draw_rectangle_filled(0, 0, 325, 325, EPS)
arcade.draw_rectangle_filled(600, 600, 325, 325, EPS)

#Circulos EPS
arcade.draw_circle_outline(300, 300, 132, EPS, 15)
arcade.draw_circle_filled(85, 515, 85, EPS)
arcade.draw_circle_filled(515, 85, 85, EPS)
#Rectangulos EPS
def generate_rect(x,y):
    arcade.draw_rectangle_filled(x,y, 325, 75, EPS)

generate_rect(0, 250)
generate_rect(0, 350)
generate_rect(600, 250)
generate_rect(600, 350)

def v_rect(x,y):
    arcade.draw_rectangle_filled(x,y, 75, 325, EPS)
v_rect(250, 0)
v_rect(350, 0)
v_rect(250, 600)
v_rect(350, 600)
arcade.finish_render()
arcade.run()