import math
import numpy as np


def min_max_normalization(arr):
    return [float(x - np.min(arr)) / (np.max(arr) - np.min(arr)) for x in arr]


def mean_normaliztion(arr):
    return [float(x - arr.mean()) / arr.std() for x in arr]


def sigmoid(arr):
    return 1. / (1 + np.exp(-arr))


def kd2kcal(kd):
    """Assume room temperature, RT=0.6"""
    return 0.6*math.log(kd*1E-9)


list = range(0, 100, 2)
# print(kd2kcal(6.4))
from rich import print
from rich.panel import Panel
from rich.console import Console
cs = Console()
print("[red]hi[/red] ff")
cs.print('hello', style=f"red")
cs.print((np.array(list)))
