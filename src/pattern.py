"""_summary_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
"""
from enum import Enum
import numpy as np


class PatternTypes(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
    """
    STILL_LIFES = 0
    OSCILLATORS = 1
    SPACESHIPS = 2


class Pattern:
    """_summary_
    """
    def __init__(self, name: str, patterntype: PatternTypes, array: np.array):
        self.name = name
        self.patterntype = patterntype
        self.array = array

    def __str__(self):
        return (
            f"{'='*40}\n"
            f"Name: {self.name}\n"
            f"Type: {self.patterntype._name_}\n"
            f"{'='*40}\n"
            f"{np.array_str(self.array).replace('0', ' ').replace('1', '#')}"
        )


class PatternInventory:
    """_summary_

    Returns:
        _type_: _description_
    """
    PATTERNS = [
        Pattern(name="block", patterntype=PatternTypes.STILL_LIFES, array=np.array([
            [1,1],
            [1,1]])),
        Pattern(name="beehive", patterntype=PatternTypes.STILL_LIFES, array=np.array([
            [0,1,1,0],
            [1,0,0,1],
            [0,1,1,0]])),
        Pattern(name="loaf", patterntype=PatternTypes.STILL_LIFES, array=np.array([
            [0,1,1,0],
            [1,0,0,1],
            [0,1,0,1],
            [0,0,1,0]])),
        Pattern(name="boat", patterntype=PatternTypes.STILL_LIFES, array=np.array([
            [1,1,0],
            [1,0,1],
            [0,1,0]])),
        Pattern(name="tub", patterntype=PatternTypes.STILL_LIFES, array=np.array([
            [0,1,0],
            [1,0,1],
            [0,1,0]])),
        Pattern(name="blinker", patterntype=PatternTypes.OSCILLATORS, array=np.array([
            [1],
            [1],
            [1]])),
        Pattern(name="toad", patterntype=PatternTypes.OSCILLATORS, array=np.array([
            [0,0,1,0],
            [1,0,0,1],
            [1,0,0,1],
            [0,1,0,0]])),
        Pattern(name="beacon", patterntype=PatternTypes.OSCILLATORS, array=np.array([
            [1,1,0,0],
            [1,1,0,0],
            [0,0,1,1],
            [0,0,1,1]])),
        Pattern(name="pulsar", patterntype=PatternTypes.OSCILLATORS, array=np.array([
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0]])),
        Pattern(name="pentadecathlon", patterntype=PatternTypes.OSCILLATORS, array=np.array([
            [0,0,0,1,0,0,0],
            [0,0,1,1,1,0,0],
            [0,1,1,0,1,1,0],
            [1,1,1,0,1,1,1],
            [1,1,1,0,1,1,1],
            [1,1,1,0,1,1,1],
            [1,1,1,0,1,1,1],
            [0,1,1,0,1,1,0],
            [0,0,1,1,1,0,0],
            [0,0,0,1,0,0,0]])),
        Pattern(name="glider", patterntype=PatternTypes.SPACESHIPS, array=np.array([
            [1,0,0],
            [0,1,1],
            [1,1,0]])),
        Pattern(name="lwss", patterntype=PatternTypes.SPACESHIPS, array=np.array([
            [0,1,1,0,0],
            [1,1,1,1,0],
            [1,1,0,1,1],
            [0,0,1,1,0]])),
        Pattern(name="mwss", patterntype=PatternTypes.SPACESHIPS, array=np.array([
            [0,0,0,1,1,0],
            [1,1,1,0,1,1],
            [1,1,1,1,1,0],
            [0,1,1,1,0,0]])),
        Pattern(name="hwss", patterntype=PatternTypes.SPACESHIPS, array=np.array([
            [0,0,0,0,1,1,0],
            [1,1,1,1,0,1,1],
            [1,1,1,1,1,1,0],
            [0,1,1,1,1,0,0]])),
    ]

    @staticmethod
    def get_patterns(n: int = 1, p: list = [1, 2, 5], replace: bool = True) -> list:
        """_summary_

        Args:
            n (int, optional): _description_. Defaults to 1.
            p (list, optional): _description_. Defaults to [1,1,1].
            replace (bool, optional): _description_. Defaults to True.

        Returns:
            list: _description_
        """
        p = [p[pattern.patterntype.value] for pattern in PatternInventory.PATTERNS]
        p /= np.sum(p)
        return np.random.choice(a=PatternInventory.PATTERNS, size=n, p=p, replace=replace)
