import pytest
from bmi_calculator import calculate_bmi, determine_weight_target

def test_calculate_bmi():
    assert calculate_bmi(60, 1.75) == pytest.approx(19.59, 0.01)

def test_determine_weight_target_underweight():
    bmi = 17
    height = 1.75
    target_weight, action = determine_weight_target(bmi, height)
    assert target_weight == pytest.approx(56.56, 0.01)
    assert action == 'gain'

def test_determine_weight_target_overweight():
    bmi = 26
    height = 1.75
    target_weight, action = determine_weight_target(bmi, height)
    assert target_weight == pytest.approx(76.26, 0.01)
    assert action == 'lose'

def test_determine_weight_target_normal():
    bmi = 22
    height = 1.75
    target_weight, action = determine_weight_target(bmi, height)
    assert target_weight is None
    assert action == 'maintain'

# Failing Test Cases

def test_calculate_bmi_with_zero_height():
    with pytest.raises(ValueError):
        calculate_bmi(60, 0)

def test_calculate_bmi_with_negative_weight():
    with pytest.raises(ValueError):
        calculate_bmi(-60, 1.75)

def test_determine_weight_target_with_invalid_bmi():
    with pytest.raises(ValueError):
        determine_weight_target(-1, 1.75)

def test_determine_weight_target_with_zero_height():
    with pytest.raises(ValueError):
        determine_weight_target(25, 0)

def test_calculate_bmi_with_zero_weight():
    with pytest.raises(ValueError):
        calculate_bmi(0, 1.75)

# This test will fail and will also fail the github actions:

# def test_calculate_bmi_with_0_height():
#     with pytest.raises(ZeroDivisionError):
#         calculate_bmi(60, 0)