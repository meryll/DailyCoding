'''
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach
the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right.
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''
import numpy as np


def get_next_points(matrix, visited, point):
    x = point[0]
    y = point[1]

    next_points = []
    add_next_point(next_points=next_points, visited=visited, matrix=matrix, point=(x - 1, y))
    add_next_point(next_points=next_points, visited=visited, matrix=matrix, point=(x + 1, y))
    add_next_point(next_points=next_points, visited=visited, matrix=matrix, point=(x, y - 1))
    add_next_point(next_points=next_points, visited=visited, matrix=matrix, point=(x, y + 1))

    return next_points


def get_next(matrix, visited, points, stop_point, step):
    if len(points) == 0: return

    all_next_points = []

    for point in points:
        if point == stop_point:
            return step
        else:
            n_points = get_next_points(matrix=matrix, visited=visited, point=point)
            all_next_points += n_points

    return get_next(matrix, visited, all_next_points, stop_point, step + 1)


def add_next_point(next_points, visited, matrix, point):
    if not (point[0] >= 0 and point[0] < matrix.shape[0] and point[1] >= 0 and point[1] < matrix.shape[1]):
        return

    if was_visied(matrix=visited, coords=point) or is_wall(matrix=matrix, coords=point):
        return

    mark_visied(matrix=visited, coords=point)
    next_points.append(point)


def mark_visied(matrix, coords):
    matrix[coords] = 1


def was_visied(matrix, coords):
    return matrix[coords] == 1


def is_wall(matrix, coords):
    return matrix[coords]


def find_path(matrix, start_point, end_point):
    matrix = np.array(matrix)
    visited = np.zeros(matrix.shape)

    mark_visied(matrix=visited, coords=start_point)
    return get_next(matrix, visited, [start], end_point, 0)


if __name__ == '__main__':

    matrix = [[False, False, False, False],
              [False, False, False, True],
              [False, False, False, False],
              [False, False, False, False]]

    start = (3, 0)
    end = (0, 0)

    step = find_path(matrix=matrix, start_point=start, end_point=end)
    print("steps", step)
