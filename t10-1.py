import arcade

arcade.open_window(300,300, "shape")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for r in range(10):
    for clm in range(10):
        y = clm * 30 +20
        x = r * 30 +15
        
        if (r+clm)%2==0:
            arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.RED,45)
        else:
            arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.BLUE,45)

arcade.finish_render()
arcade.run()
