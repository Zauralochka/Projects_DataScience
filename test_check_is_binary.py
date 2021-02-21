#production code
import numpy as np

def check_is_binary(array):
    """Checker if array consists of int or float binary values 0 (0.) and 1 (1.)
    Args:
        array (1d array-like): Array to check.
    """

    if not np.all(np.unique(array) == np.array([0, 1])):
        raise ValueError(f"Input array is not binary. "
                         f"Array should contain only int or float binary values 0 (or 0.) and 1 (or 1.). "
                         f"Got values {np.unique(array)}.")





#test code
import pytest
class TestClass:

    def test_one(self):
        a = np.random.randint(0,3,(3000,3000))
        with pytest.raises(ValueError):
            check_is_binary(a)

    def test_two(self):
       b = np.array([[0, 0], [0.0, 1]], float)
       with pytest.raises(ValueError):
            check_is_binary(b)

    def test_three(self):
        c = np.random.randint(0,2,(3000,3000))
        assert check_is_binary(c) == None