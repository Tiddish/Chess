class Chess():
    def __init__(self,row,colomn,color):
        self.row = row
        self.colomn = colomn
        self.color = color
    def __str__(self):
        return self.name


class pawn(Chess):
        def __init__(self,row,colomn,color):
            super().__init__(row,colomn,color)
            if color.upper() == "BLACK":
                self.name = "p"
            else:
                self.name = "P"
            self.firstturn = 2
        def move(self,row,colomn,deck):
            if self.color.upper() == "BLACK":
                step = -1
            else:
                step = 1
            if abs(self.row - row) <=  self.firstturn:
                if deck[row][colomn] == "." and self.colomn == colomn:
                    if deck[self.row + step][self.colomn] == ".":
                        deck[self.row][self.colomn] = "."
                        self.row = row
                        self.colomn = colomn
                        deck[row][colomn] = self
                elif deck[row][colomn] != "." and (self.row + step == row and (abs(self.colomn - colomn) == 1)) and self.color != deck[row][colomn].color:
                    deck[self.row][self.colomn] = "."
                    self.row = row
                    self.colomn = colomn
                    deck[row][colomn] = self


class Knight(Chess):
        def __init__(self,row,colomn,color):
            super().__init__(row,colomn,color)
            if color.upper() == "BLACK":
                self.name = "n"
            else:
                self.name = "N"
        def move(self,row,colomn,deck):
            if ((abs(row-self.row) == 2 and abs(colomn-self.colomn) == 1) or (abs(row-self.row) == 1 and abs(colomn-self.colomn) == 2)) and ((deck[row][colomn] == ".") or (deck[row][colomn].color != self.color)):
                deck[self.row][self.colomn] = "."
                self.row = row
                self.colomn = colomn
                deck[row][colomn] = self


class beashop(Chess):
        def __init__(self,row,colomn,color):
            super().__init__(row,colomn,color)
            if color.upper() == "BLACK":
                self.name = "b"
            else:
                self.name = "B"
        def move(self,row,colomn,deck):
            if abs(self.row - row) == abs(self.colomn - colomn):
                if self.colomn - colomn < 0:
                    stepColomn = 1
                else:
                    stepColomn = -1
                if self.row - row < 0:
                    stepRow = 1
                else:
                    stepRow = -1
                missingSpace = 0
                for i in range(1,self.colomn-colomn):
                    if deck[self.row + i*stepRow][self.colomn + i*stepColomn] != ".":
                        missingSpace = 1
                        break
                if missingSpace == 0 and (deck[row][colomn] == "." or deck[row][colomn].color != self.color):
                    deck[self.row][self.colomn] = "."
                    self.colomn = colomn
                    self.row = row
                    deck[row][colomn] = self



            



class rook(Chess):
        def __init__(self,row,colomn,color):
            super().__init__(row,colomn,color)
            if color.upper() == "BLACK":
                self.name = "r"
            else:
                self.name = "R"
        def move(self,row,colomn,deck):
            if self.row == row and self.colomn != colomn:
                step = (colomn - self.colomn) // abs(colomn - self.colomn)
                for i in range(1,abs(self.colomn-colomn)):
                    if deck[row][colomn-i*step] != ".":
                        print("2")
                        return False
                if deck[row][colomn] == "." or deck[row][colomn].color != self.color:
                    deck[self.row][self.colomn] = "."
                    self.row = row
                    self.colomn = colomn
                    deck[row][colomn] = self
            elif self.colomn == colomn and self.row != row:
                step = (row - self.row) // abs(row - self.row)
                for i in range(1,abs(self.row-row)):
                    print("2")
                    if deck[row-i*step][colomn] != ".":
                        return False
                if deck[row][colomn] == "." or deck[row][colomn].color != self.color:
                    deck[self.row][self.colomn] = "."
                    self.row = row
                    self.colomn = colomn
                    deck[row][colomn] = self
            else: print("Некоректный ввод")


class king(Chess):
    def __init__(self,row,colomn,color):
        super().__init__(row,colomn,color)
        if color.upper() == "BLACK":
            self.name = "k"
        else:
            self.name = "K"
    def move(self,row,colomn,deck):
        if abs(row - self.row) <= 1 and abs(colomn - self.colomn) <= 1 and (deck[row][colomn] == "." or deck[row][colomn].color != self.color):
            deck[self.row][self.colomn] = "."
            self.row = row
            self.colomn = colomn
            deck[row][colomn] = self
        else: print("Некоректный ввод")
    def __del__(self):
        print("king" , self.color , "повержен")

class queen(Chess):
    def __init__(self,row,colomn,color):
        super().__init__(row,colomn,color)
        if color.upper() == "BLACK":
            self.name = "q"
        else:
            self.name = "Q"
    def move(self,row,colomn,deck):
        if abs(self.row - row) == abs(self.colomn - colomn):
            if self.colomn - colomn < 0:
                stepColomn = 1
            else:
                stepColomn = -1
            if self.row - row < 0:
                stepRow = 1
            else:
                stepRow = -1
            missingSpace = 0
            for i in range(1,self.colomn-colomn):
                if deck[self.row + i*stepRow][self.colomn + i*stepColomn] != ".":
                    missingSpace = 1
                    break
            if missingSpace == 0 and (deck[row][colomn] == "." or deck[row][colomn].color != self.color):
                deck[self.row][self.colomn] = "."
                self.colomn = colomn
                self.row = row
                deck[row][colomn] = self
        elif self.row == row and self.colomn != colomn:
            step = (colomn - self.colomn) // abs(colomn - self.colomn)
            for i in range(1,abs(self.colomn-colomn)):
                if deck[row][colomn-i*step] != ".":
                    print("2")
                    return False
            if deck[row][colomn] == "." or deck[row][colomn].color != self.color:
                deck[self.row][self.colomn] = "."
                self.row = row
                self.colomn = colomn
                deck[row][colomn] = self
        elif self.colomn == colomn and self.row != row:
            step = (row - self.row) // abs(row - self.row)
            for i in range(1,abs(self.row-row)):
                print("2")
                if deck[row-i*step][colomn] != ".":
                    return False
            if deck[row][colomn] == "." or deck[row][colomn].color != self.color:
                deck[self.row][self.colomn] = "."
                self.row = row
                self.colomn = colomn
                deck[row][colomn] = self
        else: print("Некоректный ввод")




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



deck = InitialDeck()
PrintDeck(deck)
while True:
    C = input("Введите координаты: ")
    row , colomn = decoder(C)
    row1,colomn1 = decoder(input("Введите ход: "))
    deck[row][colomn].move(row1,colomn1,deck)
    PrintDeck(deck)