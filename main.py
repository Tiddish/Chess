from functionch import*
deck = InitialDeck()
PrintDeck(deck)
while True:
    C = input("Введите координаты: ")
    row , colomn = decoder(C)
    row1,colomn1 = decoder(input("Введите ход: "))
    deck[row][colomn].move(row1,colomn1,deck)
    PrintDeck(deck)