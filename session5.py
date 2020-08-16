import time


def time_it(fn, *args, repetitions=1, **kwargs):
    start_time = time.perf_counter()
    for i in range(repetitions):
        fn(*args, **kwargs)
    end_time = time.perf_counter()

    return start_time - end_time


def squared_power_list(num, start, end):
    squared_list = []
    if end == 0:
        raise ValueError("end cannot be 0.")
    if num == 0:
        raise ValueError("num cannot be 0.")
    for i in range(start, end + 1):
        squared_list.append(num ** i)

    return squared_list


def polygon_area(side_len, sides):
    if sides < 3 or sides > 6:
        raise ValueError("Number of sides cannot be less than 3 or more than 6.")
    if side_len == 0:
        raise ValueError("Length of side cannot be 0.")

    if sides == 3:
        return ((3 ** 0.5) * (side_len ** 2)) / 4
    elif sides == 4:
        return side_len * side_len
    elif sides == 5:
        return 1 / 4 * ((5 * (5 + (2 * (5 ** 0.5)))) ** 0.5) * side_len ** 2
    elif sides == 6:
        return (3 * 3 ** 0.5 * side_len ** 2) / 2


def temp_converter(temp, from_unit, to_unit):
    if from_unit not in ["c", "f", "k"] or to_unit not in ["c", "f", "k"]:
        raise ValueError("Units have to be one of c/f/k.")

    if from_unit == "c" and to_unit == "f":
        return (temp * 9 / 5) + 32
    elif from_unit == "c" and to_unit == "k":
        return temp + 273.15
    elif from_unit == "f" and to_unit == "c":
        return (temp - 32) * 5 / 9
    elif from_unit == "f" and to_unit == "k":
        return (32 * temp - 32) * (5 / 9) + 273.15
    elif from_unit == "k" and to_unit == "c":
        return temp - 273.15
    elif from_unit == "k" and to_unit == "f":
        return (temp - 273.15) * 9 / 5 + 32


def speed_converter(speed, to_distance_unit, to_time_unit):
    if speed < 0:
        raise ValueError("Speed cannot be negative.")
    if to_distance_unit not in ["km", "m", "ft", "yrd"]:
        raise ValueError("Distance unit should be one of km/m/ft/yrd.")
    if to_time_unit not in ["ms", "s", "m", "hr", "day"]:
        raise ValueError("Time unit should be one of ms/s/m/hr/day.")

    if to_distance_unit == "km":
        speed *= 1
    elif to_distance_unit == "m":
        speed *= 100
    elif to_distance_unit == "ft":
        speed *= 3280.84
    elif to_distance_unit == "yrd":
        speed *= 1093.61

    if to_time_unit == "ms":
        speed /= 60 * 60 * 100
    elif to_time_unit == "s":
        speed /= 60 * 60
    elif to_time_unit == "m":
        speed /= 60
    elif to_time_unit == "hr":
        speed *= 1
    elif to_time_unit == "day":
        speed *= 24

    return speed


print(time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=5))
