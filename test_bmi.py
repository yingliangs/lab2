from Lab2_1.bmi import calculate_bmi, classify_bmi

print("Test bmi")

def test_bmi_under_weight():
    test_bmi = -1
    bmi_value = calculate_bmi(1.73,40)
    result = classify_bmi(bmi_value)
    assert(result == test_bmi)
def test_bmi_normal_weight():
    test_bmi = 0
    bmi_value = calculate_bmi(1.73,66)
    result = classify_bmi(bmi_value)
    assert(result == test_bmi)

def test_bmi_over_weight():
    test_bmi = 1
    bmi_value = calculate_bmi(1.73,100)
    result = classify_bmi(bmi_value)
    assert(result == test_bmi)