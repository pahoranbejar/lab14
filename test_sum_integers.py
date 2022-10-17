from byu_pytest_utils import max_score, test_files, with_import


@max_score(3)
@with_import
def test_sum_integers_simple(sum_integers):
    observed = sum_integers(test_files / "sum_integers_no_words_sample.txt")
    expected = 6
    assert observed == expected


@max_score(4)
@with_import
def test_sum_integers_with_words(sum_integers):
    observed = sum_integers(test_files / "sum_integers_with_words_sample.txt")
    expected = 115
    assert observed == expected
