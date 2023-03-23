import sys

from LinkedListMazeSolver.maze_solver import AStarMazeSolver, BFSMazeSolver


def main():
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


if __name__ == "__main__":
    main()
