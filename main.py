def decoder(c):
    c = c.upper()
    if "A" <= c[0] <= "H" and 1 <= int(c[1]) <= 8:
        x = int(c[1]) - 1
        y = ord(c[0]) - ord("A") 
        return x , y


def PrintDeck(m):
    print(" ","A","B","C","D","E","F","G","H")
    for i in range(8):
        print(i+1, end = " ")
        for j in range(8):
            print(m[i][j], end = " ")
        print()


def InitialDeck():
    mass = []
    for i in range(8):
        mass.append([".",".",".",".",".",".",".","."])
    for i in range(8):
        mass[1][i] = pawn(1,i,"white")
        mass[6][i] = pawn(6,i,"black")
    mass[0][0] = rook(0,0,"white")
    mass[0][1] = Knight(0,1,"white")
    mass[0][2] = beashop(0,2,"white")
    mass[0][3] = queen(0,3,"white")
    mass[0][4] = king(0,4,"white")
    mass[0][5] = beashop(0,5,"white")
    mass[0][6] = Knight(0,6,"white")
    mass[0][7] = rook(0,7,"white")
    mass[7][0] = rook(7,0,"black")
    mass[7][1] = Knight(7,1,"black")
    mass[7][2] = beashop(7,2,"black")
    mass[7][3] = queen(7,3,"black")
    mass[7][4] = king(7,4,"black")
    mass[7][5] = beashop(7,5,"black")
    mass[7][6] = Knight(7,6,"black")
    mass[7][7] = rook(7,7,"black")
    return mass

def Won():
    pass

