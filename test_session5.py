import re
import os
import pytest
import inspect
import math
import random
import session5


README_CONTENT_CHECK_FOR = [
    "time_it",
    "squared_power_list",
    "polygon_area",
    "temp_converter",
    "speed_converter",
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
    significant indenting."""
    lines = inspect.getsource(session5)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_print():
    t = session5.time_it(print, 1, 2, 3, sep="-", end=" ***\n", repetitions=5)
    assert t != 0


def test_squared_power_list_time():
    t = session5.time_it(session5.squared_power_list, 2, start=0, end=5, repetitions=5)
    assert t != 0


def test_polygon_area_time():
    t = session5.time_it(session5.polygon_area, side_len=10, sides=6, repetitions=10)
    assert t != 0


def test_temp_converter():
    t = session5.time_it(session5.temp_converter, 0, "c", "f", repetitions=100)
    assert t != 0


def test_speed_converter_time():
    t = session5.time_it(session5.speed_converter, 10, "km", "ms", repetitions=1000)
    assert t != 0


def test_squared_power_list_end():
    with pytest.raises(ValueError):
        session5.squared_power_list(2, 0, 0)


def test_squared_power_list_num():
    with pytest.raises(ValueError):
        session5.squared_power_list(0, 1, 0)


def test_polygon_area_sides_less_than_3():
    with pytest.raises(ValueError):
        session5.polygon_area(10, 2)


def test_polygon_area_sides_more_than_6():
    with pytest.raises(ValueError):
        session5.polygon_area(10, 8)


def test_polygon_area_side_len_zero():
    with pytest.raises(ValueError):
        session5.polygon_area(0, 2)


def test_polygon_area_3():
    a = session5.polygon_area(side_len=10, sides=4)
    assert round(a) == 100


def test_polygon_area_5():
    a = session5.polygon_area(side_len=10, sides=5)
    assert round(a) == 172


def test_polygon_area_6():
    a = session5.polygon_area(side_len=10, sides=6)
    assert round(a) == 260


def test_temp_converter_units():
    with pytest.raises(ValueError):
        session5.temp_converter(10, "d", "c")


def test_temp_converter_c_f():
    assert session5.temp_converter(0, "c", "f") == 32


def test_temp_converter_c_k():
    assert session5.temp_converter(0, "c", "k") == 273.15


def test_temp_converter_f_c():
    assert round(session5.temp_converter(0, "f", "c")) == -18


def test_temp_converter_f_k():
    assert round(session5.temp_converter(0, "f", "k")) == 255


def test_temp_converter_k_c():
    assert session5.temp_converter(0, "k", "c") == -273.15


def test_temp_converter_k_f():
    assert round(session5.temp_converter(0, "k", "f")) == -460


def test_speed_converter_speed():
    with pytest.raises(ValueError):
        session5.speed_converter(-1, "m", "s")


def test_speed_converter_dist_unit():
    with pytest.raises(ValueError):
        session5.speed_converter(10, "asd", "s")


def test_speed_converter_time_unit():
    with pytest.raises(ValueError):
        session5.speed_converter(10, "m", "asd")


def test_speed_converter_km_ms():
    assert round(session5.speed_converter(10, "km", "ms")) == 0


def test_speed_converter_km_s():
    assert round(session5.speed_converter(10, "km", "s")) == 0


def test_speed_converter_km_m():
    assert round(session5.speed_converter(10, "km", "m")) == 0


def test_speed_converter_km_hr():
    assert round(session5.speed_converter(10, "km", "hr")) == 10


def test_speed_converter_km_day():
    assert round(session5.speed_converter(10, "km", "day")) == 240


def test_speed_converter_m_ms():
    assert round(session5.speed_converter(10, "m", "ms")) == 0


def test_speed_converter_m_s():
    assert round(session5.speed_converter(10, "m", "s")) == 0


def test_speed_converter_m_m():
    assert round(session5.speed_converter(10, "m", "m")) == 17


def test_speed_converter_m_hr():
    assert round(session5.speed_converter(10, "m", "hr")) == 1000


def test_speed_converter_m_day():
    assert round(session5.speed_converter(10, "m", "day")) == 24000


def test_speed_converter_ft_ms():
    assert round(session5.speed_converter(10, "ft", "ms")) == 0


def test_speed_converter_ft_s():
    assert round(session5.speed_converter(10, "ft", "s")) == 9


def test_speed_converter_ft_m():
    assert round(session5.speed_converter(10, "ft", "m")) == 547


def test_speed_converter_ft_hr():
    assert round(session5.speed_converter(10, "ft", "hr")) == 32808


def test_speed_converter_ft_day():
    assert round(session5.speed_converter(10, "ft", "day")) == 787402


def test_speed_converter_yrd_ms():
    assert round(session5.speed_converter(10, "yrd", "ms")) == 0


def test_speed_converter_yrd_s():
    assert round(session5.speed_converter(10, "yrd", "s")) == 3


def test_speed_converter_yrd_m():
    assert round(session5.speed_converter(10, "yrd", "m")) == 182


def test_speed_converter_yrd_hr():
    assert round(session5.speed_converter(10, "yrd", "hr")) == 10936


def test_speed_converter_yrd_day():
    assert round(session5.speed_converter(10, "yrd", "day")) == 262466
