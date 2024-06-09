from main import find_missing_number

# Add function param for benchmark
def test_find_missing_number():
    assert find_missing_number([0, 1, 3]) == 2

    assert find_missing_number([1, 2, 4, 5]) == 3

    assert find_missing_number([1, 3, 4, 5]) == 2

    # Ambiguous
    assert find_missing_number([1]) == 0 or find_missing_number([1]) == 2

    assert find_missing_number([0]) == -1 or find_missing_number([0]) == 1

    print("All tests have passed!")

if __name__ == "__main__":
    test_find_missing_number()
