from typing import List

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np


class MotionPlot:
    def __init__(self, linewidth=5, background_color='black', fig_size=(10, 10)):
        self.linewidth = linewidth
        self.background_color = background_color
        self.figure_size = fig_size

    def plot(self, path):
        plt.rcParams['figure.facecolor'] = self.background_color
        plt.figure(figsize=self.figure_size)
        plt.plot(path.real, path.imag, linewidth=self.linewidth)  # plotting with thick linewidth
        plt.axis('equal')  # explicitly specifying that the axes should be equal in proportion
        plt.axis('off')  # turning the visibility of x-y axes to 'off'
        plt.show()  ## finally, showing the graph


class ShapePlot:
    def __init__(self, linewidth=5, background_color='black', fig_size=(10, 10)):
        self.linewidth = linewidth
        self.background_color = background_color
        self.figure_size = fig_size

    def plot(self, shapes: List[np.ndarray], **kwargs):
        plt.rcParams['figure.facecolor'] = self.background_color
        plt.figure(figsize=self.figure_size)
        patches = list()
        color = kwargs.get("color")
        for shape in shapes:
            polygon = Polygon(np.array([shape.real, shape.imag]).T, closed=True, fill=False, linewidth=self.linewidth,color=color)
            patches.append(polygon)
        p = PatchCollection(patches, match_original=True)
        fig, ax = plt.subplots()
        ax.add_collection(p)
        plt.axis('equal')  # explicitly specifying that the axes should be equal in proportion
        plt.axis('off')  # turning the visibility of x-y axes to 'off'
        plt.show()  ## finally, showing the graph
