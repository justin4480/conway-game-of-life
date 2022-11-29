An optimised python implementation of [Conways Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) that uses:
- numpy / scipy for the world simulation
- pygame for the view

Configurable parameters (located in __main__.py) are:

# Screen config
WIDTH = 500
HEIGHT = 500
PIXEL_SIZE = 1
FPS = 120

# Pattern config
N_PATTERNS = 500
P_PATTERNS = [0.1, 0.1, 0.8]

Running _main__.py will


# Patterns:

``` python
from src.pattern import PATTERN_INVENTORY

for p in PATTERN_INVENTORY:
    print(p)
```

\>>
``` python
Name: lwss
Type: SPACESHIPS
========================================
[[  # #    ]
 [# # # #  ]
 [# #   # #]
 [    # #  ]]
```
