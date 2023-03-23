# Linked-List Maze Solver

This python class provides an A* algorithm to solve linked list, represented as a dictonary, mazes. It can be used to find the shortest path between a start and end point in a maze.

The LinkedListMazeSolver class is optimized for readability and performance. It has been designed to work with mazes that contain linked list representations with no x,y,z coordinates.

## Usage

```python
from LinkedListMazeSolver import AStarMazeSolver, BFSMazeSolver

maze = {
    "A": {"exit": {"n": "B", "e": "D", "w": "C", "ne": "G", "nw": "F"}},
    "B": {"exit": {"s": "A"}},
    "C": {"exit": {"e": "A"}},
    "D": {"exit": {"w": "A", "ne": "G", "se": "H", "u": "K"}},
    "E": {"exit": {"n": "F", "e": "H", "ne": "I"}},
    "F": {"exit": {"s": "E", "ne": "G", "se": "C"}},
    "G": {"exit": {"s": "A", "nw": "F", "sw": "E"}},
    "H": {"exit": {"w": "D", "n": "I", "nw": "E"}},
    "I": {"exit": {"s": "H", "sw": "D"}},
    "J": {"exit": {"n": "K", "e": "L"}},
    "K": {"exit": {"s": "J", "d": "D"}},
    "L": {"exit": {"w": "J", "e": "M"}},
    "M": {"exit": {"w": "L"}},
}

solver = AStarMazeSolver(maze, "A", "M")
result = solver.solve()
print(result)
solver = BFSMazeSolver(maze, "A", "M")
result = solver.solve()
print(result)
```
## Output
```python
e u s e e
e u s e e
```

## Supported Maze Directions

This implementation was designed with a maze containing the following directions: 
```
n, s, e, w, ne, nw, se, sw, u, d
```
However, you may define your own directions in your sample data.

### Customization

If you need to customize the behavior of the BidirectionalAStarMazeSolver class, you can do so by subclassing the class and overriding its methods.

For example, if you want to use a different heuristic function, you can override the __heuristic__ method:
```python
class CustomMazeSolver(AStarMazeSolver):
    def __heuristic__(self, curr, end, maze):
        # Custom heuristic function
        pass
```


## Contributions

Contributions to the MazeSolver class are welcome! If you find a bug or want to suggest a new feature, please open an issue or submit a pull request on Github.

## License

This implementation is licensed under the MIT License.
