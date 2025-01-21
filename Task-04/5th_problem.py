def can_place_word_horizontally(grid, word, row, col):
    if col + len(word) > 10:
        return False

    for i in range(len(word)):
        if grid[row][col + i] not in ('-', word[i]):
            return False

    return True

def can_place_word_vertically(grid, word, row, col):
    if row + len(word) > 10:
        return False

    for i in range(len(word)):
        if grid[row + i][col] not in ('-', word[i]):
            return False

    return True

def place_word_horizontally(grid, word, row, col):
    for i in range(len(word)):
        grid[row][col + i] = word[i]

def place_word_vertically(grid, word, row, col):
    for i in range(len(word)):
        grid[row + i][col] = word[i]

def remove_word_horizontally(grid, word, row, col):
    for i in range(len(word)):
        if grid[row][col + i] == word[i]:
            grid[row][col + i] = '-'

def remove_word_vertically(grid, word, row, col):
    for i in range(len(word)):
        if grid[row + i][col] == word[i]:
            grid[row + i][col] = '-'

def solve_crossword(grid, words, index):
    if index == len(words):
        return True

    word = words[index]

    for row in range(10):
        for col in range(10):
            if can_place_word_horizontally(grid, word, row, col):
                place_word_horizontally(grid, word, row, col)
                if solve_crossword(grid, words, index + 1):
                    return True
                remove_word_horizontally(grid, word, row, col)

            if can_place_word_vertically(grid, word, row, col):
                place_word_vertically(grid, word, row, col)
                if solve_crossword(grid, words, index + 1):
                    return True
                remove_word_vertically(grid, word, row, col)

    return False

def crossword_puzzle(grid, words):
    words = words.split(';')
    solve_crossword(grid, words, 0)
    return grid

if __name__ == "__main__":
    # Input the grid
    grid = [list(input().strip()) for _ in range(10)]

    # Input the words
    words = input().strip()

    # Solve the crossword puzzle
    solved_grid = crossword_puzzle(grid, words)

    # Print the solved grid
    for row in solved_grid:
        print(''.join(row))
