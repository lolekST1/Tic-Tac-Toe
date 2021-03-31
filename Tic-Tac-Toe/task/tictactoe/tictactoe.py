# write your code here

cells = [" " for _ in range(9)]


def arrayprint():
    index = 0
    array = [[x for x in range(3)] for _ in range(3)]
    print("---------")
    for a in range(3):
        print("|", end=" ")
        for b in range(3):
            print(cells[index], end=" ")
            array[a][b] = cells[index]
            index += 1
        print("|")
    print("---------")


def move(z):
    global tura
    coord_l = input("Enter the coordinates:").split()
    try:
        coord = [int(x) for x in coord_l]
    except ValueError:
        print("You should enter numbers!")
        move(z)
        return

    if coord[0] < 1 or coord[0] > 3 or coord[1] < 1 or coord[1] > 3:
        print("Coordinates should be from 1 to 3!")
        move(z)
        return
    else:
        new = (coord[0] - 1) * 3 + (coord[1] - 1)

    if cells[new] == " ":
        cells[new] = z
        if tura == "X":
            tura = "O"
        else:
            tura = "X"
    else:
        print("This cell is occupied! Choose another one!")
        move(z)
        return


def who_wins():
    global winner
    is_winner = 0
    for z in ["X", "O"]:
        w = [z, z, z]
        if cells[:3] == w or cells[3:6] == w or cells[6:] == w:
            is_winner = 1
            winner = z
        if cells[:7:3] == w or cells[1:8:3] == w or cells[2:9:3] == w:
            is_winner = 1
            winner = z
        if cells[::4] == w or cells[2:7:2] == w:
            is_winner = 1
            winner = z
    # xs = cells.count("X")
    # os = cells.count("O")
    # if is_winner > 1 or abs(xs - os) > 1:
    #    print("Impossible")
    if is_winner == 1:
        print(f"{winner} wins")
    elif is_winner == 0 and " " not in cells:
        print("Draw")
        winner = "Draw"


winner = None
tura = "X"
arrayprint()
while winner is None:
    if tura == "X":
        move("X")
    else:
        move("O")
    arrayprint()
    who_wins()
