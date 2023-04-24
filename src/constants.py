"""
File to define constant variables to use in the scripts.
"""
from dataclasses import dataclass


@dataclass
class ConstantVariables:
    """
    Dataclass to define variables for the project.

    Variables:
        e2 (float): energy.
        k0 (float): plank constant.
    """
    e2: float = 0.1 ** 2
    k0: float = 100.00
