n = 8
desk = [[0 for i in range(n)] for j in range(n)]


def print_desk(desk):
    for i in range(n):
        print(desk[i])


def put(desk, x, y):
    for i in range(n):
        desk[i][y] += 1
    for j in range(n):
        desk[x][j] += 1

    if y >= x:
        for j in range(y-x, n, +1):
            desk[j-(y-x+1)+1][j] += 1
    if y < x:
        for i in range(x-y, n, +1):
            desk[i][i-(x-y+1)+1] += 1

    if x + y < n:
        for j in range(y+x, -1, -1):
            desk[(y+x)-j][j] += 1
    if x + y >= n:
        for i in range(x+y-n+1, n, +1):
            desk[i][n-(i-(x+y-n))] += 1

    desk[x][y] = -1


def remove(desk, x, y):
    for i in range(n):
        desk[i][y] -= 1
    for j in range(n):
        desk[x][j] -= 1

    if y >= x:
        for j in range(y-x, n, +1):
            desk[j-(y-x+1)+1][j] -= 1
    if y < x:
        for i in range(x-y, n, +1):
            desk[i][i-(x-y+1)+1] -= 1

    if x + y < n:
        for j in range(y+x, -1, -1):
            desk[(y+x)-j][j] -= 1
    if x + y >= n:
        for i in range(x+y-n+1, n, +1):
            desk[i][n-(i-(x+y-n))] -= 1

    desk[x][y] = 0


def solution(i):
    for j in range(8):
        if desk[i][j] == 0:
            put(desk, i, j)
            if i == 7:
                print_desk(desk)
                return
            else:
                # print_desk(desk)
                # print("")
                solution(i + 1)
            # print("remove")
            remove(desk, i, j)


solution(0)