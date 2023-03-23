import queue

invert = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
    "northeast": "southwest",
    "southwest": "northeast",
    "northwest": "southeast",
    "southeast": "northwest",
    "below": "above",
    "above": "below",
    "up": "down",
    "down": "up",
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e",
    "ne": "sw",
    "sw": "ne",
    "nw": "se",
    "se": "nw",
    "u": "d",
    "d": "u"
}


class BFSMazeSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.path = queue.Queue()
        self.visited = set()

        if start not in maze:
            raise Exception(f"{start} not in maze")
        elif end not in maze:
            raise Exception(f"{end} not in maze")

    def _find_end(self, moves):
        loc, _ = self._navigate_maze(moves)
        return loc == self.end

    def _valid(self, moves):
        _, valid = self._navigate_maze(moves)
        return valid

    def _navigate_maze(self, current_loc, move):
        if current_loc not in self.maze or move not in self.maze[current_loc]["exit"] or self.maze[current_loc]["exit"][move] == "":
            return current_loc, False
        return self.maze[current_loc]["exit"][move], True

    def solve(self):
        self.path.put(("", self.start))
        self.visited.add(self.start)
        while not self.path.empty():
            moves, current_pos = self.path.get()
            if current_pos == self.end:
                return moves
            for d in self.maze[current_pos]["exit"]:
                next_pos, is_valid = self._navigate_maze(current_pos, d)
                if is_valid and next_pos not in self.visited:
                    next_moves = f"{moves} {d}".strip()
                    self.visited.add(next_pos)
                    self.path.put((next_moves, next_pos))
        return None


class AStarMazeSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end

        if start not in maze:
            raise Exception(f"{start} not in maze")
        elif end not in maze:
            raise Exception(f"{end} not in maze")

    @staticmethod
    def __get_neighbors__(maze, curr):
        neighbors = []
        if curr not in maze:
            return neighbors
        for d, room in maze[curr]["exit"].items():
            if room:
                neighbors.append(room)
        return neighbors

    def __heuristic__(self, curr, end):
        visited = {curr}
        maze = self.maze
        distance = 0
        next_layer = self.__get_neighbors__(maze, curr)
        while next_layer:
            curr_layer = next_layer
            next_layer = []
            for node in curr_layer:
                if node == end:
                    return distance + 1
                for neighbor in self.__get_neighbors__(maze, node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_layer.append(neighbor)
            distance += 1
        return float("inf")

    @staticmethod
    def __reconstruct_path__(came_from, current_node):
        path = []
        while current_node in came_from:
            prev_node, move = came_from[current_node]
            path.append(move)
            current_node = prev_node
        return ' '.join(reversed(path))

    def __neighbor_nodes__(self, room):
        neighbors = []
        for direction, neighbor_id in self.maze[room]["exit"].items():
            if neighbor_id is not None:
                neighbors.append((neighbor_id, direction))  # Include the direction
        return neighbors

    def solve(self):
        open_set = queue.PriorityQueue()
        closed_set = set()

        open_set.put((0, self.start))

        g_score = {self.start: 0}
        came_from = {}

        while not open_set.empty():
            current = open_set.get()[1]

            if current == self.end:
                return self.__reconstruct_path__(came_from, current)

            closed_set.add(current)

            for neighbor, direction in self.__neighbor_nodes__(current):
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = (current, direction)
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.__heuristic__(neighbor, self.end)
                    open_set.put((f_score, neighbor))

        return None
