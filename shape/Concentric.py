import numpy as np
from typing import Union, List
import random


class ConcentricPolygon:
    def __init__(self, edges: Union[List[int], np.ndarray] = None, regular: bool = True, align: bool = False,
                 separation: str = "uniform", min_increase: float = 1, max_separation: float = 1) -> object:
        """
        :param edges: A 1D list specifying the number of edges on each shape from inside out.
        :param regular: tells whether the polygons themselves should be regular or not.
        :param align: tell whether atleast one of the vertex of all the shapes should be aligned.
        :param separation:
        ::uniform: the distance of vertex from origin will increase uniformly for each shape.
        ::irregular: the distance of vertex from origin will increase by a random amount.
        """
        self.edges = np.array(edges).flatten()
        self.regular = regular
        self.separation = separation
        self.align = align
        self.min_increase = min_increase
        self.max_separation = max_separation
        if separation not in ("uniform", "irregular"):
            raise ValueError("separation should be one of acceptable values")
        self.uniform_separation = separation == "uniform"

    def get_shapes(self):
        shapes = list()
        for (i, x) in enumerate(range(self.edges.shape[0])):
            variation_separation = random.uniform(0,1) * (self.max_separation if not self.uniform_separation else 0)
            separation_width = self.min_increase * (i+1) + variation_separation
            rotation = 2 * np.pi * 1j if self.align else 1j*random.uniform(0,2 * np.pi)
            directions = np.exp(1j * np.linspace(0, 2 * np.pi, self.edges[i] + 1) + rotation)[:-1]
            shapes.append(separation_width * directions)
        return shapes

