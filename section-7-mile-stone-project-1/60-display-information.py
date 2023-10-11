def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
display(row1, row2, row3)

row3[2] = 'X'
row1[0] = 'O'
print('\n')
display(row1, row2, row3)
