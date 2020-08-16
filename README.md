# Session 5

This is the readme for session-5.
This file contains information for functions present in `session5.py` and `test_session5.py`.

## Run Tests 

```
pytest -v  
```


## Functions in `session5.py`.


The function defitions are as follows: 

### time_it(fn, *args, repetitions=1, **kwargs)
Function to time other functions. Accepts a function on of it's inputs.

### squared_power_list(num, start, end)
Raise a given number from numbers `start` and `end`.

### polygon_area(side_len, sides)
Calculate area of polygons with sides ranging from 3 to 6.

### temp_converter(temp, from_unit, to_unit)
Convert temperature between K, F, and C.

### speed_converter(speed, to_distance_unit, to_time_unit)
Convert speed between different units. dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph.



## Functions in `test_session5.py`.


The test definitions are as follows: 

### test_readme_exists():
Checks if README exists.

### test_readme_contents():
Check if README.md file is interesting! Should have atleast 500 words.


### test_readme_proper_description()
Describe all the functions/class well in your README.md file.


### test_readme_file_for_formatting():
README has atleast 10 "#".

### test_indentations():
Code indentation should follow PEP8 guidelines.


### test_function_name_had_cap_letter():
No Capital letter(s) in your function names.

### test_squared_power_list_end()
End number cannot be 0.

### test_squared_power_list_num()
Verify square power list.

### test_polygon_area_sides_less_than_3()
Number of sides cannot be less than 3.

### test_polygon_area_sides_more_than_6()
Number of sides cannot be more than 6.

### test_polygon_area_side_len_zero()
Length of polygon cannot be 0.

### test_polygon_area_3()
Verify area of polygon of size 3.

### test_polygon_area_4()
Verify area of polygon of size 4.

### test_polygon_area_5()
Verify area of polygon of size 5.

### test_polygon_area_6()
Verify area of polygon of size 6.


### test_temp_converter_units()
Units can only be K/C/F.

### test_temp_converter_c_f()
Verify conversion results of temperature conversion.

### test_temp_converter_c_k()
Verify conversion results of temperature conversion.


### test_temp_converter_f_c()
Verify conversion results of temperature conversion.


### test_temp_converter_f_k()
Verify conversion results of temperature conversion.


### test_temp_converter_k_c()
Verify conversion results of temperature conversion.


### test_temp_converter_k_f()
Verify conversion results of temperature conversion.


### test_speed_converter_speed()
Verify conversion results of speed conversion.


### test_speed_converter_dist_unit()
Verify conversion results of speed conversion.


### test_speed_converter_time_unit()
Verify conversion results of speed conversion.


### test_speed_converter_km_ms()
Verify conversion results of speed conversion.


### test_speed_converter_km_s()
Verify conversion results of speed conversion.


### test_speed_converter_km_m()
Verify conversion results of speed conversion.


### test_speed_converter_km_hr()
Verify conversion results of speed conversion.


### test_speed_converter_km_day()
Verify conversion results of speed conversion.


### test_speed_converter_m_ms()
Verify conversion results of speed conversion.


### test_speed_converter_m_s()
Verify conversion results of speed conversion.


### test_speed_converter_m_m()
Verify conversion results of speed conversion.


### test_speed_converter_m_hr()
Verify conversion results of speed conversion.


### test_speed_converter_m_day()
Verify conversion results of speed conversion.


### test_speed_converter_ft_ms()
Verify conversion results of speed conversion.


### test_speed_converter_ft_s()
Verify conversion results of speed conversion.

### test_speed_converter_ft_m()
Verify conversion results of speed conversion.

### test_speed_converter_ft_hr()
Verify conversion results of speed conversion.


### test_speed_converter_ft_day()
Verify conversion results of speed conversion.


### test_speed_converter_yrd_ms()
Verify conversion results of speed conversion.


### test_speed_converter_yrd_s()
Verify conversion results of speed conversion.


### test_speed_converter_yrd_m()
Verify conversion results of speed conversion.


### test_speed_converter_yrd_hr()
Verify conversion results of speed conversion.


### test_speed_converter_yrd_day()
Verify conversion results of speed conversion.

