from Lab2_1.exercise3 import calc_average_temperature, calc_median_temp, find_min_max

print("Test Lab2 exercise 3")



def test_calc_average_temperature():
    
    result = calc_average_temperature([4.0,5.0,6.0,7.0])
    expected = 5.5
    assert(result == expected)
def test_find_min_max():
    result = find_min_max([4.0,5.0,2.0])
    expected = 2.0,5.0
    assert(result == expected)


def test_calc_median_temp():
    result = calc_median_temp([2.0,3.0,4.0,5.0])
    expected = 3.5
    assert(result == expected)




