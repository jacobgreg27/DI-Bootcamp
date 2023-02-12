matrix = [
    "7i3",
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

def decode_matrix(matrix):
    columns = len(matrix[0])
    rows = len(matrix)
    message = ""

    for col in range(columns):
        for row in range(rows):
            char = matrix[row][col]
            if char.isalpha():
                message += char
                if row < rows-1 and not matrix[row+1][col].isalpha():
                    message += " "
    return message

print(decode_matrix(matrix))

