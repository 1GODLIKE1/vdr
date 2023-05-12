import os
import numpy as np


class Release:
    def __init__(self, RELEASE_PATH):
        self.RELEASE_PATH = RELEASE_PATH

    def release(self):
        dirs = np.array([])
        for list in os.listdir(self.RELEASE_PATH):
            if os.path.isdir(list):
                dirs = np.append(dirs, list.replace("5.06.", ""))
        return max(dirs)