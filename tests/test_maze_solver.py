from unittest import TestCase
from LinkedListMazeSolver.maze_solver import AStarMazeSolver, BFSMazeSolver


class TestMazeSolver(TestCase):
    def test_astar_solve(self):
        maze = {
            "A": {"exit": {"n": "B", "e": "D", "w": "C", "ne": "G", "nw": "F"}},
            "B": {"exit": {"s": "A"}},
            "C": {"exit": {"e": "A"}},
            "D": {"exit": {"w": "A", "ne": "G", "se": "H", "u": "K"}},
            "E": {"exit": {"n": "F", "e": "H", "ne": "I"}},
            "F": {"exit": {"s": "E", "ne": "G", "se": "C"}},
            "G": {"exit": {"s": "A", "nw": "F", "sw": "E", "e": "H", "n": "I", "ne": "J", "w": "K", "s": "L", "se": "M",
                           "u": "S"}},
            "H": {"exit": {"w": "D", "n": "I", "nw": "E"}},
            "I": {
                "exit": {"s": "H", "sw": "D", "s": "J", "e": "K", "se": "L", "ne": "M", "n": "S", "nw": "T", "w": "R"}},
            "J": {"exit": {"n": "K", "e": "L", "w": "I", "nw": "M"}},
            "K": {"exit": {"s": "J", "d": "D", "e": "G"}},
            "L": {"exit": {"w": "J", "e": "M", "s": "I", "se": "S", "n": "T", "ne": "U"}},
            "M": {"exit": {"w": "L", "nw": "J", "n": "I", "ne": "S", "d": "G"}},
            "R": {"exit": {"e": "I"}},
            "S": {"exit": {"n": "G", "e": "M", "w": "I"}},
            "T": {"exit": {"s": "L", "e": "U", "se": "V", "w": "W"}},
            "U": {"exit": {"n": "I", "e": "V", "w": "T"}},
            "V": {"exit": {"w": "U", "n": "L", "nw": "T", "ne": "S", "se": "W"}},
            "W": {"exit": {"e": "T", "s": "V", "w": "X"}},
            "X": {"exit": {"e": "W"}},
        }

        start = "A"
        end = "X"
        solver = AStarMazeSolver(maze, start, end)
        result = solver.solve()
        self.assertIsNotNone(result)
        moves = result.split()
        print("moves:", moves)


        current_room = start
        for move in moves:
            next_room = maze[current_room]["exit"].get(move)
            self.assertIsNotNone(next_room, f"Invalid move '{move}' at room {current_room}")
            current_room = next_room

        self.assertEqual(end, current_room, "Path does not reach the end point")

    def test_bfs_solve(self):
        maze = {
            "A": {"exit": {"n": "B", "e": "D", "w": "C", "ne": "G", "nw": "F"}},
            "B": {"exit": {"s": "A"}},
            "C": {"exit": {"e": "A"}},
            "D": {"exit": {"w": "A", "ne": "G", "se": "H", "u": "K"}},
            "E": {"exit": {"n": "F", "e": "H", "ne": "I"}},
            "F": {"exit": {"s": "E", "ne": "G", "se": "C"}},
            "G": {"exit": {"s": "A", "nw": "F", "sw": "E", "e": "H", "n": "I", "ne": "J", "w": "K", "s": "L", "se": "M",
                           "u": "S"}},
            "H": {"exit": {"w": "D", "n": "I", "nw": "E"}},
            "I": {
                "exit": {"s": "H", "sw": "D", "s": "J", "e": "K", "se": "L", "ne": "M", "n": "S", "nw": "T", "w": "R"}},
            "J": {"exit": {"n": "K", "e": "L", "w": "I", "nw": "M"}},
            "K": {"exit": {"s": "J", "d": "D", "e": "G"}},
            "L": {"exit": {"w": "J", "e": "M", "s": "I", "se": "S", "n": "T", "ne": "U"}},
            "M": {"exit": {"w": "L", "nw": "J", "n": "I", "ne": "S", "d": "G"}},
            "R": {"exit": {"e": "I"}},
            "S": {"exit": {"n": "G", "e": "M", "w": "I"}},
            "T": {"exit": {"s": "L", "e": "U", "se": "V", "w": "W"}},
            "U": {"exit": {"n": "I", "e": "V", "w": "T"}},
            "V": {"exit": {"w": "U", "n": "L", "nw": "T", "ne": "S", "se": "W"}},
            "W": {"exit": {"e": "T", "s": "V", "w": "X"}},
            "X": {"exit": {"e": "W"}},
        }

        start = "A"
        end = "X"
        solver = BFSMazeSolver(maze, start, end)
        result = solver.solve()
        self.assertIsNotNone(result)
        moves = result.split()
        print("moves:", moves)


        current_room = start
        for move in moves:
            next_room = maze[current_room]["exit"].get(move)
            self.assertIsNotNone(next_room, f"Invalid move '{move}' at room {current_room}")
            current_room = next_room

        self.assertEqual(end, current_room, "Path does not reach the end point")
