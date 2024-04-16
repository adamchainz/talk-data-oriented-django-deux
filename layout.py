# Row-oriented

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


from random import random

points = [
    Point(random(), random())
    for _ in range(10_000)
]


def mean_point():
    return Point(
        sum(p.x for p in points) / len(points),
        sum(p.y for p in points) / len(points),
    )


# Column-oriented

xs = []
ys = []


for _ in range(10_000):
    xs.append(random())
    ys.append(random())


def mean_point2():
    return (
        sum(xs) / len(xs),
        sum(ys) / len(ys),
    )


# Column-oriented arrays

import polars as pl


# Generate 10,000 random 2D points
points_dataframe = pl.DataFrame({
    'x': [random() for _ in range(10_000)],
    'y': [random() for _ in range(10_000)]
})


def mean_point3():
    return (
        points_dataframe['x'].mean(),
        points_dataframe['y'].mean(),
    )
