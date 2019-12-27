import matplotlib.animation as manimation
import random
import numpy as np

from matplotlib import pyplot as plt
from config.confg import *


class BoardService(object):

    def __init__(self, board):
        self._board = board

    def create_array(self):
        array = np.zeros((self._board.get_cols(), self._board.get_rows()))
        self._board.set_array(array)
        return self._board

    def fill_random_cells(self):
        for x in range(self._board.cols):
            for y in range(self._board.rows):
                self._board.array[x][y] = random.getrandbits(1)
        return self._board

    def generate_video(self, max_steps):
        def board_iterator(array, max_steps):
            for _ in range(max_steps):
                sum = BoardService.count_alive(array)
                array = np.logical_or(np.logical_and(array, sum == 2), sum == 3)
                array = array.astype(int)
                yield array

        FFMpegWriter = manimation.writers[video_codec]
        metadata = dict(title=video_title)
        writer = FFMpegWriter(fps=video_fps, metadata=metadata)
        fig = plt.figure()
        fig.patch.set_facecolor(video_face_color)

        with writer.saving(fig, video_name + video_extension, video_dpi):
            plt.spy(self._board.get_array())
            plt.axis(video_axis)
            writer.grab_frame()
            plt.clf()
            for element in board_iterator(self._board.get_array(), max_steps):
                plt.spy(element)
                plt.axis(video_axis)
                writer.grab_frame()
                plt.clf()
        return self._board

    @staticmethod
    def count_alive(array):
        def roll_element(x, y):
            return np.roll(np.roll(array, y, axis=0), x, axis=1)

        sum = roll_element(1, 0) + roll_element(0, 1) + roll_element(-1, 0) \
              + roll_element(0, -1) + roll_element(1, 1) + roll_element(-1, -1) \
              + roll_element(1, -1) + roll_element(-1, 1)
        return sum
