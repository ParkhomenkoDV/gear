from math import nan, pi
from typing import Dict

ENGINS = (
    # 370
    {"power": 370, "frequency": 1000, "name": "71A4", "rf": 915},
    # 550
    {"power": 550, "frequency": 1500, "name": "71A4", "rf": 1357},
    {"power": 550, "frequency": 1000, "name": "71B6", "rf": 915},
    # 750
    {"power": 750, "frequency": 3000, "name": "71A2", "rf": 2820},
    {"power": 750, "frequency": 1500, "name": "71B4", "rf": 1350},
    {"power": 750, "frequency": 1000, "name": "80A6", "rf": 920},
    {"power": 750, "frequency": 750, "name": "90LA8", "rf": 705},
    # 1100
    {"power": 1100, "frequency": 3000, "name": "71B2", "rf": 2805},
    {"power": 1100, "frequency": 1500, "name": "80A4", "rf": 1395},
    {"power": 1100, "frequency": 1000, "name": "80B6", "rf": 920},
    {"power": 1100, "frequency": 750, "name": "90LB8", "rf": 715},
    # 1500
    {"power": 1500, "frequency": 3000, "name": "80A2", "rf": 2850},
    {"power": 1500, "frequency": 1500, "name": "80B4", "rf": 1395},
    {"power": 1500, "frequency": 1000, "name": "90L6", "rf": 925},
    {"power": 1500, "frequency": 7500, "name": "100L8", "rf": 702},
    # 2200
    {"power": 2200, "frequency": 3000, "name": "80B2", "rf": 2850},
    {"power": 2200, "frequency": 1500, "name": "90L4", "rf": 1395},
    {"power": 2200, "frequency": 1000, "name": "100L6", "rf": 945},
    {"power": 2200, "frequency": 750, "name": "112MA8", "rf": 709},
    # 3000
    {"power": 3000, "frequency": 3000, "name": "90L2", "rf": 2850},
    {"power": 3000, "frequency": 1500, "name": "100S4", "rf": 1410},
    {"power": 3000, "frequency": 1000, "name": "112MA6", "rf": 950},
    {"power": 3000, "frequency": 750, "name": "112MB8", "rf": 709},
    # 4000
    {"power": 4000, "frequency": 3000, "name": "100L2", "rf": 2850},
    {"power": 4000, "frequency": 1500, "name": "100L4", "rf": 1410},
    {"power": 4000, "frequency": 1000, "name": "112MB6", "rf": 950},
    {"power": 4000, "frequency": 750, "name": "132S8", "rf": 716},
    # 5500
    {"power": 5500, "frequency": 3000, "name": "100S2", "rf": 2850},
    {"power": 5500, "frequency": 1500, "name": "112M4", "rf": 1432},
    {"power": 5500, "frequency": 1000, "name": "132S6", "rf": 960},
    {"power": 5500, "frequency": 750, "name": "132M8", "rf": 712},
    # 7500
    {"power": 7500, "frequency": 3000, "name": "112M2", "rf": 2895},
    {"power": 7500, "frequency": 1500, "name": "132S4", "rf": 1440},
    {"power": 7500, "frequency": 1000, "name": "132M6", "rf": 960},
    {"power": 7500, "frequency": 750, "name": "160S8", "rf": 727},
    # 11000
    {"power": 11000, "frequency": 3000, "name": "132M2", "rf": 2910},
    {"power": 11000, "frequency": 1500, "name": "132M4", "rf": 1447},
    {"power": 11000, "frequency": 1000, "name": "160S6", "rf": 970},
    {"power": 11000, "frequency": 750, "name": "160M8", "rf": 727},
    # 15000
    {"power": 15000, "frequency": 3000, "name": "160S2", "rf": 2910},
    {"power": 15000, "frequency": 1500, "name": "160S4", "rf": 1455},
    {"power": 15000, "frequency": 1000, "name": "160M6", "rf": 970},
    {"power": 15000, "frequency": 750, "name": "180M8", "rf": 731},
    # 18500
    {"power": 18500, "frequency": 3000, "name": "160M2", "rf": 2910},
    {"power": 18500, "frequency": 1500, "name": "160M4", "rf": 1455},
    {"power": 18500, "frequency": 1000, "name": "180M6", "rf": 980},
    # 22000
    {"power": 22000, "frequency": 3000, "name": "180S2", "rf": 2919},
    {"power": 22000, "frequency": 1500, "name": "180S4", "rf": 1462},
    # 30000
    {"power": 30000, "frequency": 3000, "name": "180M2", "rf": 2925},
    {"power": 30000, "frequency": 1500, "name": "180M4", "rf": 1470},
)
for e in ENGINS:
    e["frequency"] *= 2 * pi / 60  # перевод в рад/с
    e["rf"] *= 2 * pi / 60  # перевод в рад/с

U1 = [1, 1.25, 1.6, 2, 2.5, 3.15, 4, 5, 6.3, 12.5, 16, 20, 25, 31.5, 40, 50, 63, 80]  # 1 ряд
U2 = [1.12, 1.4, 1.8, 2.24, 2.8, 3.55, 4.5, 5.6, 14, 18, 22.4, 26, 35.5, 45, 56, 71]  # 2 ряд
U = tuple(sorted(U1 + U2))

# ГОСТ 6636-69
Ra40 = (20, 22, 24, 25, 26, 28, 30, 32, 34, (35), 36, 38, 40, 42, 45, 48, 50, 53, (55), 56, 60, 63, (65), 67, (70), 71, 75, 80, 85, 90, 95, 100)

# ГОСТ 8752-79
d_cuff = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 30, 32, 34, 35, 36, 38, 40, 42, 44, 45, 48, 50, 52, 55, 56, 58, 60, 62, 63, 65, 70, 71, 75, 80, 82, 85)


def get_f(d: float) -> float:
    if 17 <= d <= 22:
        return 1.0
    if 24 <= d <= 30:
        return 1.0
    if 32 <= d <= 38:
        return 1.2
    if 40 <= d <= 44:
        return 1.2
    if 45 <= d <= 50:
        return 1.6
    if 52 <= d <= 58:
        return 2.0
    if 60 <= d <= 65:
        return 2.0
    if 67 <= d <= 75:
        return 2.5
    if 80 <= d <= 85:
        return 2.5
    if 90 <= d <= 95:
        return 3.0
    return nan


def get_spline(d: float) -> Dict[str, float]:
    """Получение размеров шпонки по диаметру"""
    if 12 <= d < 17:
        return {"b": 5.0, "h": 5, "t1": 3.0, "l_min": 10, "l_max": 56}
    if 17 <= d < 22:
        return {"b": 6.0, "h": 6, "t1": 3.5, "l_min": 14, "l_max": 70}
    if 22 <= d < 30:
        return {"b": 8.0, "h": 7, "t1": 4.0, "l_min": 18, "l_max": 90}
    if 30 <= d < 38:
        return {"b": 10.0, "h": 8, "t1": 5.0, "l_min": 28, "l_max": 110}
    if 38 <= d < 44:
        return {"b": 12.0, "h": 8, "t1": 5.0, "l_min": 28, "l_max": 140}
    if 44 <= d < 50:
        return {"b": 14.0, "h": 9, "t1": 5.5, "l_min": 36, "l_max": 160}
    if 50 <= d < 58:
        return {"b": 16.0, "h": 10, "t1": 6.0, "l_min": 45, "l_max": 180}
    if 58 <= d < 65:
        return {"b": 18.0, "h": 11, "t1": 7.0, "l_min": 50, "l_max": 200}
    if 65 <= d < 75:
        return {"b": 20.0, "h": 12, "t1": 7.5, "l_min": 56, "l_max": 220}
    if 75 <= d < 85:
        return {"b": 22.0, "h": 14, "t1": 9.0, "l_min": 63, "l_max": 250}
    if 85 <= d < 95:
        return {"b": 25.0, "h": 14, "t1": 9.0, "l_min": 70, "l_max": 280}
    return {}


def get_bearing(d: float) -> Dict[str, float]:
    """Получение размеров П по его диамтеру посадки"""
    if d <= 0:
        raise Exception(f"Диаметр {d=} должен быть больше 0")
    if d % 5 != 0:
        raise Exception(f"Диаметр {d=} должен быть кратен 5")

    return {}


def get_cuff(d: float) -> Dict[str, float]:
    """Получение манжеты по ее диамтеру посадки"""
    if d <= 0:
        raise Exception(f"Диаметр {d=} должен быть больше 0")
    if d not in d_cuff:
        raise Exception(f"Диаметр {d=} не сущетсвует в ГОСТ 8752-79")
    elif d == 6:
        return {"D": 22, "h": 7}
    elif d == 7:
        return {"D": 22, "h": 7}
    elif d == 8:
        return {"D": 22, "h": 7}
    elif d == 9:
        return {"D": 22, "h": 7}
    elif d == 10:
        return {"D": 26, "h": 7}
    elif d == 11:
        return {"D": 26, "h": 7}
    elif d == 12:
        return {"D": 28, "h": 7}
    elif d == 13:
        return {"D": 28, "h": 7}
    elif d == 14:
        return {"D": 28, "h": 7}
    elif d == 15:
        return {"D": 30, "h": 7}
    elif d == 15:
        return {"D": 32, "h": 7}
    elif d == 16:
        return {"D": 30, "h": 7}
    elif d == 16:
        return {"D": 32, "h": 7}
    elif d == 17:
        return {"D": 32, "h": 7}
    elif d == 18:
        return {"D": 35, "h": 7}
    elif d == 19:
        return {"D": 35, "h": 7}
    elif d == 20:
        return {"D": 35, "h": 7}
    elif d == 20:
        return {"D": 40, "h": 10}
    elif d == 21:
        return {"D": 40, "h": 10}
    elif d == 22:
        return {"D": 40, "h": 10}
    else:
        return {}
