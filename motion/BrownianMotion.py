import numpy as np


class BrownianMotion:
    def __init__(self, step_size=0.1, num_directions=4):
        self.step_size = step_size
        self.number_directions = num_directions

    def get_motion_path(self, iter_num):
        directions = np.exp(1j * np.linspace(0, 2 * np.pi, self.number_directions + 1))[:-1]
        path = np.zeros(iter_num, dtype='complex128')
        for i in range(1, iter_num):
            path[i] = path[i - 1] + self.step_size * np.random.choice(directions)
        return path
