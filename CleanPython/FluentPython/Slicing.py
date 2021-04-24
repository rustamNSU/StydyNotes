s = 'bicycle'
print('s[::3] =', s[::3])
print('s[::-1] =', s[::-1])
print('s[-1::-1] =', s[-1::-1])

invoice = """
    0.....6.................................40........52...55........
    1909  Pimoroni PiBrella                     $17.50    3    $52.50
    1489  6mm Tactile Switch x20                 $4.95    2     $9.90
    1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
    1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


# Multi-dimensional slicing and ellipsis
# in numpy  x[i, ...] <=> x[i, :, :, :]

# Assigning slices
l = list(range(10))
l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

l[2:5] = (100,)
print(l)

l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd')


# Building lists of lists
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'O'
print(weird_board)
"""
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
"""
