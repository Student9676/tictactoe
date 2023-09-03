"""
Tic Tac Toe Player
"""

import copy
import math

X = 'X'
O = 'O'
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY,
            EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if terminal(board) is True:
        return None
    if empty(board) is True:
        return X
    elif X_on_board(board) == O_on_board(board):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board) is True:
        return None

    x_list = []
    y_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                x_list.append(i)
                y_list.append(j)

    actions = []
    for i in range(len(x_list)):
        actions.append((x_list[i], y_list[i]))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise AttributeError(str(action)
                             + ' is not a valid action for the board')

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    X_count = 0
    O_count = 0
    for i in range(3):
        if board[i][i] == X:
            X_count += 1
        if board[i][i] == O:
            O_count += 1
    if X_count == 3:
        return X
    if O_count == 3:
        return O

    X_count = 0
    O_count = 0
    for i in range(3):
        if board[i][2 - i] == X:
            X_count += 1
        if board[i][2 - i] == O:
            O_count += 1
    if X_count == 3:
        return X
    if O_count == 3:
        return O

    for i in range(3):
        X_count = 0
        O_count = 0
        for j in range(3):
            if board[i][j] == X:
                X_count += 1
            if board[i][j] == O:
                O_count += 1
        if X_count == 3:
            return X
        if O_count == 3:
            return O

    for i in range(3):
        X_count = 0
        O_count = 0
        for j in range(3):
            if board[j][i] == X:
                X_count += 1
            if board[j][i] == O:
                O_count += 1
        if X_count == 3:
            return X
        if O_count == 3:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) is X:
        if empty(board):
            return (0, 0)

        v = minValue(result(board, actions(board)[0]))
        best_action = actions(board)[0]
        for action in actions(board):
            if minValue(result(board, action)) > v:
                v = minValue(result(board, action))
                best_action = action
            if v == 1:
                return action
        return best_action
    else:

        v = maxValue(result(board, actions(board)[0]))
        best_action = actions(board)[0]
        for action in actions(board):
            if maxValue(result(board, action)) < v:
                v = maxValue(result(board, action))
                best_action = action
            if v == -1:
                return action
        return best_action


def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
        if v == 1:
            return 1
    return v


def minValue(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
        if v == -1:
            return -1
    return v


def empty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                return False

    return True


def X_on_board(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count += 1

    return count


def O_on_board(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == O:
                count += 1

    return count
