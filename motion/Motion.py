from abc import ABC, abstractmethod
import numpy as np


class Algorithm(ABC):
    @abstractmethod
    def get_next_step(self):
        pass


class Motion(Algorithm):
    def __init__(self, num_steps, path=None):
        self.steps = int(num_steps)
        try:
            if path is not None:
                path = np.array(path, dtype='complex128')
                if path.ndim != 1:
                    raise Exception("path should have only 1 dimension")
                path = np.append(path, np.zeros(self.steps))[:self.steps]
            else:
                path = np.zeros(self.steps, dtype='complex128')
        except TypeError as e:
            print(e)
            path = np.zeros(self.steps, dtype='complex128')
        self.path = path

    @abstractmethod
    def get_next_step(self):
        pass

    def get_motion_path(self):
        motion_path = np.zeros(self.steps,dtype='complex128')
        for i in range(1, self.steps):
            motion_path[i] = motion_path[i-1] + self.get_next_step()
        return self.path + motion_path
