"""
Generate potential well or step.
"""
import numpy as np
from typing import List


class Potential:
    """
    Class to generate potential well (V0 negative) or step (V0 positive).
    """
    @staticmethod
    def generate_potential(
        N: int,
        V0: float,
        v_start: int,
        v_end: int
    ) -> np.ndarray:
        """
        Generate a numpy array representing the potential.

        Args:
            N (int): number of points.
            V0 (float): potential value.
            v_start (int): x-absis to start of the potential well or step.
            v_end (int): x-absis to end of the potential well or step.

        Returns:
            np.ndarray: numpy array representing the potential created.
        """
        potential: List[float] = []
        for i in range(N):
            if v_start <= i <= v_end:
                potential.append(V0)
            else:
                potential.append(0.0)
        return np.array(potential)
