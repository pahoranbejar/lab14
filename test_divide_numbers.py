from byu_pytest_utils import max_score, compare_files, test_files, with_import


@max_score(4)
@with_import
def test_divide_numbers(divide_numbers):
    divide_numbers(test_files / "divide_numbers_no_nan_sample.txt", test_files / "observed5.txt")
    compare_files(test_files / "divide_numbers_no_nan_expected.txt", test_files / "observed5.txt")


@max_score(4)
@with_import
def test_divide_numbers_with_nan(divide_numbers):
    divide_numbers(test_files / "divide_numbers_with_nan_sample.txt", test_files / "observed6.txt")
    compare_files(test_files / "divide_numbers_with_nan_expected.txt", test_files / "observed6.txt")