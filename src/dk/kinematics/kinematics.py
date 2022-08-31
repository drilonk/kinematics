import numpy as np
import pandas as pd


class TranslatingCordinateSystem:

    def __init__(self, r_a = None, v_a = None, a_a = None):
        self.r_a = r_a
        self.v_a = v_a
        self.a_a = a_a

    def translations(self):
        r_b = self.r_a
