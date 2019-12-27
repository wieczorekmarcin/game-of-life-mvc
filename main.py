from config.confg import *
from controller.board_controller import BoardController
from model.board import Board
from view.board_view import BoardView

if __name__ == '__main__':
    board = Board(board_cols, board_rows)
    view = BoardView()

    controller = BoardController(board, view)
    controller.create_array()

    board.get_array()[23, 22:24] = 1
    board.get_array()[24, 21:23] = 1
    board.get_array()[25, 22] = 1

    controller.generate_video(video_max_steps)
