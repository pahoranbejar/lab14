from byu_pytest_utils import max_score, test_files, with_import


def get_words(input_file):
    with open(input_file) as file:
        list_of_words = []
        for line in file:
            line = line.strip().split()
            list_of_words.extend(line)
    return list_of_words


@max_score(4)
@with_import
def test_replace_word_simple(replace_word):
    replace_word(test_files / "replace_word_simple_sample.txt", test_files / "observed3.txt", "MEOW")
    modified_words = get_words(test_files / "observed3.txt")
    for new_word in modified_words:
        assert new_word == "MEOW"


@max_score(4)
@with_import
def test_replace_word_variety(replace_word):
    replace_word(test_files / "replace_word_variety_sample.txt", test_files / "observed4.txt", "MEOW")
    input_words = get_words(test_files / "replace_word_variety_sample.txt")
    modified_words = get_words(test_files / "observed4.txt")
    for old_word, new_word in zip(input_words, modified_words):
        if old_word != new_word:
            assert new_word == "MEOW"
