from byu_pytest_utils import max_score, with_import


@max_score(7)
@with_import
def test_random_asterisks(random_asterisks):
    text = " ".join(["a" * i for i in range(1000)])
    output = random_asterisks(text)
    assert len(output.split()) == len(text.split())
    number = 0
    for item in zip(text.split(), output.split()):
        assert len(item[0]) == len(item[1])
        if "*" in item[1]:
            number += 1
    assert 200 < number < 400
