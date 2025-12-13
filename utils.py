def choice(value, values, method: str):
    """Выбор значения из списка по методу"""

    METHODS = ("floor", "nearest", "ceil")

    assert isinstance(values, (tuple, list))
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
