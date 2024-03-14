import turtle

screen = turtle.Screen()
turtle.screensize(canvwidth=800, canvheight=800)
IMAGE = 'India_map_blank.gif'
screen.title("INDIA States Quiz")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
