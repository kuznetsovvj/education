# https://leetcode.com/problems/word-search/

# Классический перебор с возвратами (как в задаче с ферзями)

def exist(board, word):
    def check_next_char(pos_char, curr_pos):
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_pos_x = curr_pos[0] + dx
            new_pos_y = curr_pos[1] + dy
            if 0 <= new_pos_x < len(board) and 0 <= new_pos_y < len(board[0]):
                if board[new_pos_x][new_pos_y] == word[pos_char]:
                    if (new_pos_x, new_pos_y) not in path:
                        path.add((new_pos_x, new_pos_y))
                        
                        if pos_char == len(word) - 1:
                            return True

                        if check_next_char(pos_char + 1, (new_pos_x, new_pos_y)):
                            return True
        path.remove(curr_pos)
        return False

    path = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                # важно не потерять кейс с шаблоном из одного символа
                if len(word) == 1:
                    return True
                path.add((i, j))
                if check_next_char(1, (i, j)):
                    return True
    return False

assert exist(board = [['A', 'B', 'D'], ['B', 'D', 'R'], ['C', 'B', 'R']], word = 'ABC') == True
assert exist(board = [['A', 'B', 'C'], ['B', 'D', 'R'], ['B', 'B', 'R']], word = 'ABC') == True