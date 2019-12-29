# Game of Life

Implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) in MVC architecture.
It was invented by John Horton Conway, a British mathematician, in 1970.
It takes place on a square grid of cells, where each cell can be either alive or dead. Their behavior is governed by the following rules:
- cell comes alive when it has exactly three neighbors alive,
- cell survives when it has two or three live neighbors (it dies when it has fewer than two - from loneliness, or when it has more than four - from overcrowding).
