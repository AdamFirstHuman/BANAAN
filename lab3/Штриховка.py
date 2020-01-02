from graph import*

x1 = 225
y1 = 260
dx = 3
dy = 2


x2 = 75
y2 = 160
n = 0

while n < 300:

    line(x1, y1, x2, y2)
    x1 = x1 + dx
    y1 = y1 + dy
    x2 = x2 + dx
    y2 = y2 + dy
    n = n + 1






run()