from service.board_service import BoardService


class BoardController(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.service = BoardService(self.model)

    def create_array(self):
        self.view.show_create_board_array_info()
        board = self.service.create_array()
        return board

    def generate_video(self, max_steps):
        self.view.show_generate_video_info()
        board = self.service.generate_video(max_steps)
        return board

    def fill_random_cells(self):
        self.view.show_fill_board_info()
        board = self.service.fill_random_cells()
        return board

    def count_alive(self, cols, rows):
        self.view.show_count_alive_board_info()
        board = self.service.count_alive(cols, rows)
        return board
