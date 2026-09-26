from app import check_grammar


def test_grammar_correction():
    assert check_grammar("She go to school yesterday.") == "She went to school yesterday."


def test_grammar_correction_2():
    assert check_grammar("He go to school every day.") == "He goes to school every day."


def test_grammar_correction_3():
    assert check_grammar("I has a book.") == "I have a book."


def test_grammar_correction_4():
    assert check_grammar("They is happy.") == "They are happy."
