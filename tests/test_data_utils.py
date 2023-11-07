from sedaro.results.utils import to_time_major

def test_to_time_major():
    assert to_time_major(True) == True # items other than lists or dicts are returned as is
    assert to_time_major([1, 2, 3]) == [1, 2, 3]
    assert to_time_major([[1, 2], [3, 4], [5, 6]]) == ([[1, 3, 5], [2, 4, 6]])
    assert to_time_major([[[1, 5], [2, 6]], [[3, 7], [4, 8]]]) == [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

def run_tests():
    test_to_time_major()

run_tests()