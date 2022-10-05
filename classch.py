from main import deck

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
