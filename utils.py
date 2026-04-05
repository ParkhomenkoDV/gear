from itertools import product
from math import prod
from typing import List, Tuple, Union


def choice(value, values: Union[List, Tuple], method: str) -> float | int:
    """Выбор значения из списка по методу"""

    METHODS = ("floor", "nearest", "ceil")

    assert isinstance(value, (int, float)), f"{type(value)=} must be numeric"
    assert isinstance(values, (tuple, list)), f"{type(values)=} must be tuple"
    assert method in METHODS

    if method == "floor":
        for v in values[::-1]:
            if v <= value:
                return v
    elif method == "ceil":
        for v in values:
            if v >= value:
                return v
    elif method == "nearest":
        best = values[0]
        for v in values[1:]:
            if abs(v - value) < abs(best - value):
                best = v
        return best
    else:
        raise ValueError(f"{method=} not in {METHODS}")


def find_best_product(a: float, *numbers: List[float]) -> Tuple[Tuple[float], float]:
    """Подбор лучшей комбинации n множителей из numbers для произведния a"""

    if not numbers:
        raise ValueError("Списоков нет")
    for i, lst in enumerate(numbers):
        if not lst:
            raise ValueError(f"Список {i} пустой")

    best_combination = None
    best_product = 0
    min_relative_error = float("inf")

    for combo in product(*numbers):
        product_val = prod(combo)

        # Используем относительную ошибку
        if a != 0:
            relative_error = abs((product_val - a) / a)
        else:
            relative_error = abs(product_val)

        if relative_error < min_relative_error:
            min_relative_error = relative_error
            best_combination = combo
            best_product = product_val

    return (tuple(best_combination), best_product)
