# Conway's Game of Life (simulator)

![](/assets/main.gif)

### What is [Conways Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)?

Devised by British mathematician [John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in 1970, Game of Life is zero player game whereby an initial configuation is seeded on a 2 dimensional matrix in which each cells is either live or dead.  On each iteration of time, each cell interacts with it's eight immediate neigbours and the cells state changed based on the four rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Set up

To run, simply clone the repo, ensure to pip | conda install the three packages listed in the requirements.txt and run the \_\_main__.py file.

# Implementation

This implementation prioritised optimisation which was achieved using:
- numpy / scipy for the world simulation
- pygame for the view

Note. A working tensorflow simulation is also included; but commented out to avoid the need to include tensorflow in the requirements.txt.

# Configurable parameters
Located in __main__.py, there are some basic configurable parameters.

### <B>Screen config:</B>
Standard view parameters.  Increasing screen resolution will impact performance, however on my non GPU dell XPS I can comfortable hit 120 FPS based on the below default config.
``` python
# __main__.py line 10
# Screen config
WIDTH = 500
HEIGHT = 500
PIXEL_SIZE = 1  # increase to 2 or 3 if performance is an issue
FPS = 120       # set to -1 to run at maximum FPS
```

### <B>Pattern config:</B>
The number of patterns to seed the world with and the proportion of each pattern type {pixel, still lifes, oscillators, spaceships}
``` python
# __main__.py line 16
# Pattern config
N_PATTERNS = 500                   # number of patterns
P_PATTERNS = [0.1, 0.1, 0.1, 0.7]  # proportion of patterns (by type)
```


### Example configurations:
Below are some example initial world configurations and 200 frame screenshot gifs.

``` python
# Pattern config
N_PATTERNS = 30000
P_PATTERNS = [1.0, 0.0, 0.0, 0.0]
```
![](/assets/example1.gif)

``` python
# Pattern config
N_PATTERNS = 1000
P_PATTERNS = [0.25, 0.25, 0.25, 0.25]
```
![](/assets/example2.gif)

``` python
# Pattern config
N_PATTERNS = 500
P_PATTERNS = [0.1, 0.1, 0.1, 0.7]
```
![](/assets/example3.gif)

# Patterns:

The world is seeded (populated) with 'patterns'.  Here are all the patterns:

``` python
from src.pattern import PATTERN_INVENTORY

for p in PATTERN_INVENTORY:
    print(p)
```



\>>
``` python
========================================
Name: block
Type: PIXEL
========================================
[[#]]
```
\>>
``` python
========================================
Name: block
Type: STILL_LIFES
========================================
[[# #]
 [# #]]
```
``` python
========================================
Name: beehive
Type: STILL_LIFES
========================================
[[  # #  ]
 [#     #]
 [  # #  ]]
```
``` python
========================================
Name: loaf
Type: STILL_LIFES
========================================
[[  # #  ]
 [#     #]
 [  #   #]
 [    #  ]]
```
``` python
========================================
Name: boat
Type: STILL_LIFES
========================================
[[# #  ]
 [#   #]
 [  #  ]]
```
``` python
========================================
Name: tub
Type: STILL_LIFES
========================================
[[  #  ]
 [#   #]
 [  #  ]]
```
``` python
========================================
Name: blinker
Type: OSCILLATORS
========================================
[[#]
 [#]
 [#]]
```
``` python
========================================
Name: toad
Type: OSCILLATORS
========================================
[[    #  ]
 [#     #]
 [#     #]
 [  #    ]]
```
``` python
========================================
Name: beacon
Type: OSCILLATORS
========================================
[[# #    ]
 [# #    ]
 [    # #]
 [    # #]]
```
``` python
========================================
Name: pulsar
Type: OSCILLATORS
========================================
[[    # # #       # # #    ]
 [                         ]
 [#         #   #         #]
 [#         #   #         #]
 [#         #   #         #]
 [    # # #       # # #    ]
 [                         ]
 [    # # #       # # #    ]
 [#         #   #         #]
 [#         #   #         #]
 [#         #   #         #]
 [                         ]
 [    # # #       # # #    ]]
```
``` python
========================================
Name: pentadecathlon
Type: OSCILLATORS
========================================
[[      #      ]
 [    # # #    ]
 [  # #   # #  ]
 [# # #   # # #]
 [# # #   # # #]
 [# # #   # # #]
 [# # #   # # #]
 [  # #   # #  ]
 [    # # #    ]
 [      #      ]]
```
``` python
========================================
Name: glider
Type: SPACESHIPS
========================================
[[#    ]
 [  # #]
 [# #  ]]
```
``` python
========================================
Name: lwss
Type: SPACESHIPS
========================================
[[  # #    ]
 [# # # #  ]
 [# #   # #]
 [    # #  ]]
```
``` python
========================================
Name: mwss
Type: SPACESHIPS
========================================
[[      # #  ]
 [# # #   # #]
 [# # # # #  ]
 [  # # #    ]]
```
``` python
========================================
Name: hwss
Type: SPACESHIPS
========================================
[[        # #  ]
 [# # # #   # #]
 [# # # # # #  ]
 [  # # # #    ]]
```
