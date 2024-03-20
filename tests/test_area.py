import pytest  
import math
from src.area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])


def test_calculate_area_square_correct():
    # Given
    side_length = 5
    area = calculate_area_square(side_length)
    assert area == 33