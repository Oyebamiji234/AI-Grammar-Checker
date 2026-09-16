from app import check_grammar

def test_grammar_correction():
    result = check_grammar("She go to school yesterday.")
    assert result == "She went to school yesterday."