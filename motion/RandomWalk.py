import numpy as np
from .Motion import Motion


class RandomWalk(Motion):
    def __init__(self, num_steps, step_size=0.1, num_directions=4, **kwargs):
        super().__init__(num_steps, **kwargs)
        self.step_size = step_size
        self.number_directions = num_directions
        self.directions = np.exp(1j * np.linspace(0, 2 * np.pi, self.number_directions + 1))[:-1]

    def get_next_step(self):
        return self.step_size * np.random.choice(self.directions)
