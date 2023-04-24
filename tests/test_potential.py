"""
Test file to test the generation of the potential.
"""
import pytest
from src.potential import Potential
import numpy as np


@pytest.mark.parametrize("N, V0, v_start, v_end", [
    (20, 1, 10, 15),
    (20, -1, 10, 15),
])
def test_generate_potential(
    N: int,
    V0: float,
    v_start: int,
    v_end: int
) -> None:
    """
    Test to check that the potential is generated correctly.

    Args:
        N (int): number of points.
        V0 (float): potential value.
        v_start (int): x-absis to start of the potential well or step.
        v_end (int): x-absis to end of the potential well or step.
    """
    potential = Potential.generate_potential(N, V0, v_start, v_end)
    assert np.all(potential[v_start:v_end] == V0)
    assert np.all(potential[:v_start] == 0)
    assert np.all(potential[v_end + 1:] == 0)
