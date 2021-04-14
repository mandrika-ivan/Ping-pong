import tkinter

# ???????
WIDTH = 840
HEIGHT = 450
d = -1.01
# ШАРИК
ballX = WIDTH / 2
ballY = HEIGHT / 2
ballR = 10
# РАКЕТКИ
r1X = 0
r1Y = 0
r2X = WIDTH
r2Y = HEIGHT - 100
lX = 20
lY = 80
# СКОРОСТИ
v_x = 6
v_y = 2
v_1 = 0
v_2 = 0
# СЧЁТ
red = 0
blue = 0

window = tkinter.Tk()
window.title('Ping-pong')
window.geometry('840x450')

canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg="green")
canvas.pack()
# Надпись
win = canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('Purisa', 20), fill='orange', text='')
# Линии на поле
canvas.create_rectangle(0, 0, WIDTH + 10, 5, fill='white', outline='white')
canvas.create_rectangle(0, HEIGHT - 5, WIDTH + 10, HEIGHT + 10, fill='white', outline='white')
canvas.create_rectangle(0, 0, 5, HEIGHT + 10, fill='white', outline='white')
canvas.create_rectangle(WIDTH - 5, 0, WIDTH + 10, HEIGHT + 10, fill='white', outline='white')
canvas.create_rectangle(0, HEIGHT / 2 - 1, WIDTH + 10, HEIGHT / 2 + 1, fill='white', outline='white')
canvas.create_rectangle(WIDTH / 2 - 1, 0, WIDTH / 2 + 10, HEIGHT + 1, fill='gray', outline='white')
# Счёт
count_red = canvas.create_text(WIDTH / 2 - 40, 50, font=('Purisa', 15), fill='red', text=red)
count_blue = canvas.create_text(WIDTH / 2 + 40, 50, font=('Purisa', 15), fill='blue', text=blue)


# def count():
#     global blue, red, count_red, count_blue
#     count_red = canvas.create_text(WIDTH/2 - 40, 50, font=('Purisa', 15), fill='red', text=red)
#     count_blue = canvas.create_text(WIDTH / 2 + 40, 50, font=('Purisa', 15), fill='blue', text=blue)
#     canvas.after(1000, count)


def f(e):
    print()


def restart(e):
    global red, blue, ballX, ballY, ball, count_blue, count_red
    window.bind("<space>", f)
    red = 0
    blue = 0
    canvas.delete(count_red)
    canvas.delete(count_blue)
    canvas.delete(Text1)
    canvas.delete(Text2)
    canvas.delete(Text3)
    canvas.delete(Text4)
    ballX = WIDTH / 2
    ballY = HEIGHT / 2
    ball = canvas.create_oval(ballX - ballR, ballY - ballR, ballX + ballR, ballY + ballR, fill="yellow")
    count_red = canvas.create_text(WIDTH / 2 - 40, 50, font=('Purisa', 15), fill='red', text=red)
    count_blue = canvas.create_text(WIDTH / 2 + 40, 50, font=('Purisa', 15), fill='blue', text=blue)
    print(1)


def game_over_rw():
    global ball, v_x, v_y, Text1, Text2, Text3, Text4
    Text1 = canvas.create_text(WIDTH / 2, HEIGHT / 3, font=('Purisa', 30), fill='orange', text='GAME OVER')
    Text4 = canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('Purisa', 20, "bold"), fill='red', text='RED        ')
    Text2 = canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('Purisa', 20, 'bold'), fill='orange', text='         WIN')
    Text3 = canvas.create_text(WIDTH / 2, 2 * HEIGHT / 3, font=('Purisa', 15), fill='yellow',
                               text='PRESS SPACE TO RESTART')
    window.bind("<space>", restart)


def game_over_bw():
    global ball, v_x, v_y, Text1, Text2, Text3, Text4
    Text1 = canvas.create_text(WIDTH / 2, HEIGHT / 3, font=('Purisa', 30), fill='orange', text='GAME OVER')
    Text4 = canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('Purisa', 20, 'bold'), fill='blue', text='BLUE          ')
    Text2 = canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('Purisa', 20, 'bold'), fill='orange', text='         WIN')
    Text3 = canvas.create_text(WIDTH / 2, 2 * HEIGHT / 3, font=('Purisa', 15), fill='yellow',
                               text='PRESS SPACE TO RESTART')
    window.bind("<space>", restart)


def red_win():
    global ballX, ballY, ball, ballR, v_x, v_y, win, red, count_red
    canvas.delete(ball)
    red += 1
    if red == 10:
        game_over_rw()
        red += 1
    elif red < 10:
        canvas.delete(count_red)
        count_red = canvas.create_text(WIDTH / 2 - 40, 50, font=('Purisa', 15), fill='red', text=red)
        ballX = WIDTH / 2
        ballY = HEIGHT / 2
        v_x = 0
        v_y = 0
        win = canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('Purisa', 20), fill='red', text='RED WIN')
        canvas.after(2000, remove_rw)


def blue_win():
    global ballX, ballY, ball, ballR, v_x, v_y, win, blue, count_blue
    canvas.delete(ball)
    blue += 1
    if blue == 10:
        blue += 1
        game_over_bw()
    elif blue < 10:
        canvas.delete(count_blue)
        count_blue = canvas.create_text(WIDTH / 2 + 40, 50, font=('Purisa', 15), fill='blue', text=blue)
        ballX = WIDTH / 2
        ballY = HEIGHT / 2
        v_x = 0
        v_y = 0
        win = canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('Purisa', 20), fill='blue', text='BLUE WIN')
        canvas.after(2000, remove_bw)


def remove_rw():
    global ballX, ballY, ball, ballR, v_x, v_y, win
    canvas.delete(win)
    ball = canvas.create_oval(ballX - ballR, ballY - ballR, ballX + ballR, ballY + ballR, fill="yellow")
    v_x = -6
    v_y = -2


def remove_bw():
    global ballX, ballY, ball, ballR, v_x, v_y, win
    canvas.delete(win)
    ball = canvas.create_oval(ballX - ballR, ballY - ballR, ballX + ballR, ballY + ballR, fill="yellow")
    v_x = 6
    v_y = 3


# НЕНУЖНО
# def remove():
#     global ballX, ballY, ball, ballR, v_x, v_y, win
#     canvas.delete(win)
#     # canvas.after(1000, game_over)
#
#
# def text():
#     global win
#     win = canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('Purisa', 20), fill='orange', text='GAME OVER')
#     canvas.after(1000, remove)


def move_ball():
    global ballX, ballY, v_x, v_y, d, r1X, r2X, r1Y, r2Y, v_1, v_2
    canvas.move(ball, v_x, v_y)
    ballX += v_x
    ballY += v_y
    if ballY + ballR > HEIGHT:
        v_y = v_y * d
    elif ballY - ballR < 1:
        v_y = v_y * d
        if v_2 > 0:
            v_y = v_y + 3
        elif v_2 < 0:
            v_y = v_y - 3
    elif ballX - ballR < r1X + lX and r1Y < ballY < r1Y + lY:
        v_x = v_x * d
        if v_1 > 0:
            v_y = v_y + 2
        elif v_1 < 0:
            v_y = v_y - 2
    elif ballX + ballR > WIDTH - lX and r2Y < ballY < r2Y + lY:
        v_x = v_x * d
    elif ballX + ballR < 0:
        blue_win()
    elif ballX - ballR > WIDTH:
        red_win()
    canvas.after(10, move_ball)


def racket_move():
    global racket1, v_1, r1Y, lY, HEIGHT, v_2, r2Y
    if (r1Y + lY < HEIGHT and v_1 > 0) or (r1Y > 0 and v_1 < 0):
        canvas.move(racket1, 0, v_1)
        r1Y += v_1
    if (r2Y + lY < HEIGHT and v_2 > 0) or (r2Y > 0 and v_2 < 0):
        canvas.move(racket2, 0, v_2)
        r2Y += v_2
    canvas.after(10, racket_move)


#
# НЕНУЖНО
# def racket_move():
#     global racket1, v_1, r1Y, lY, HEIGHT, v_2, r2Y
#     if (r1Y >= 0 and r1Y + lY < HEIGHT) or (r1Y < 0 and v_1 > 0):
#         canvas.move(racket1, 0, v_1)
#         r1Y += v_1
#         # canvas.move(racket2, 0, v_2)
#         # r2Y += v_2
#     elif r1Y < 0:
#         # canvas.move(racket1, 0, -v_r)
#         # r1Y -=v_r
#         v_1=0
#         canvas.configure()
#     canvas.after(10, racket_move)


# НЕНУЖНО
# def racket1_move_down(e):
#     global r1Y
#     if e.keycode == 87:
#         r1Y -= 10
#         canvas.move(racket1, 0, -10)
#     elif e.keycode == 83:
#         r1Y += 10
#         canvas.move(racket1, 0, 10)

# window.bind("<KeyPress>", racket1_move_down)


def move(e):
    global v_1, v_2
    if e.keycode == 83:
        v_1 = 10
    elif e.keycode == 87:
        v_1 = -10
    elif e.keycode == 79:
        v_2 = -10
    elif e.keycode == 76:
        v_2 = 10
    print("move")


def stop(e):
    global v_1, v_2
    if e.keycode == 83 and v_1 > 0 or e.keycode == 87 and v_1 < 0:
        v_1 = 0
    elif e.keycode == 79 and v_2 < 0 or e.keycode == 76 and v_2 > 0:
        v_2 = 0
    print("stop")


window.bind("<KeyPress>", move)

window.bind("<KeyRelease>", stop)

ball = canvas.create_oval(ballX - ballR, ballY - ballR, ballX + ballR, ballY + ballR, fill="yellow")
racket1 = canvas.create_rectangle(r1X, r1Y, r1X + lX, r1Y + lY, fill="red")
racket2 = canvas.create_rectangle(r2X - lX, r2Y + lY, r2X, r2Y, fill="blue")

racket_move()
move_ball()

window.mainloop()
