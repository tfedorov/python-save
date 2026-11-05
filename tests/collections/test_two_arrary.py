import pytest


def calculate(nums: list[int], target):
    already_find = {}
    for el_idx in range(len(nums)):
        el = nums[el_idx]
        need_to_find = target - el
        if need_to_find in already_find:
            return (already_find[need_to_find], el_idx)
        el_to_match = el
        already_find[el_to_match] = el_idx
    return (-1, -1)


def test_calculate_success():
    input_nums: list[int] = [2, 7, 11, 15]
    input_target = 9

    result: tuple[int, int] = calculate(input_nums, input_target)

    expected: tuple[int, int] = (0, 1)
    assert result == expected


def test_calculate_failed_empty():
    input_nums: list[int] = []
    input_target = 9

    result: tuple[int, int] = calculate(input_nums, input_target)

    expected: tuple[int, int] = (-1, -1)
    assert result == expected


def test_calculate_success_last():
    input_nums: list[int] = [2, 7, 11, 15]
    input_target = 26

    result: tuple[int, int] = calculate(input_nums, input_target)

    expected: tuple[int, int] = (2, 3)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
