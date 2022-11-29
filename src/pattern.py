from enum import Enum

import numpy as np


class PatternTypes(Enum):
    STILL_LIFES = 0
    OSCILLATORS = 1
    SPACESHIPS = 2


class Pattern:
    def __init__(self, name: str, patterntype: PatternTypes, array: np.array) -> None:
        self.name = name
        self.patterntype = patterntype
        self.array = array

    def get_array(self) -> np.array:
        return self.array

    def __str__(self) -> str:
        return (
            f"{'='*40}\n"
            f"Name: {self.name}\n"
            f"Type: {self.patterntype._name_}\n"
            f"{'='*40}\n"
            f"{np.array_str(self.array).replace('0', ' ').replace('1', '#')}"
        )


def get_patterns(n_patterns: int = 1, p_patterns: list = None, replace: bool = True) -> list:
    p_patterns = p_patterns if p_patterns else len(PATTERN_INVENTORY) * [1]
    p_patterns = [p_patterns[pattern.patterntype.value] for pattern in PATTERN_INVENTORY]
    p_patterns /= np.sum(p_patterns)
    patterns = np.random.choice(a=PATTERN_INVENTORY, size=n_patterns, p=p_patterns, replace=replace)
    return [pattern.get_array() for pattern in patterns]


PATTERN_INVENTORY = [
    Pattern(name="block", patterntype=PatternTypes.STILL_LIFES, array=np.array([
        [1, 1],
        [1, 1]])),
    Pattern(name="beehive", patterntype=PatternTypes.STILL_LIFES, array=np.array([
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]])),
    Pattern(name="loaf", patterntype=PatternTypes.STILL_LIFES, array=np.array([
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 0]])),
    Pattern(name="boat", patterntype=PatternTypes.STILL_LIFES, array=np.array([
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 0]])),
    Pattern(name="tub", patterntype=PatternTypes.STILL_LIFES, array=np.array([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]])),
    Pattern(name="blinker", patterntype=PatternTypes.OSCILLATORS, array=np.array([
        [1],
        [1],
        [1]])),
    Pattern(name="toad", patterntype=PatternTypes.OSCILLATORS, array=np.array([
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 0]])),
    Pattern(name="beacon", patterntype=PatternTypes.OSCILLATORS, array=np.array([
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]])),
    Pattern(name="pulsar", patterntype=PatternTypes.OSCILLATORS, array=np.array([
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]])),
    Pattern(name="pentadecathlon", patterntype=PatternTypes.OSCILLATORS, array=np.array([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]])),
    Pattern(name="glider", patterntype=PatternTypes.SPACESHIPS, array=np.array([
        [1, 0, 0],
        [0, 1, 1],
        [1, 1, 0]])),
    Pattern(name="lwss", patterntype=PatternTypes.SPACESHIPS, array=np.array([
        [0, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0]])),
    Pattern(name="mwss", patterntype=PatternTypes.SPACESHIPS, array=np.array([
        [0, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0]])),
    Pattern(name="hwss", patterntype=PatternTypes.SPACESHIPS, array=np.array([
        [0, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 0]])),
]
