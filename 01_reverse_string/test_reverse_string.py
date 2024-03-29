import types
from reverse_string import reverse

def test_reverse_function_exist():
    assert isinstance(reverse, types.FunctionType)

def test_reverse():
    assert reverse("apple") == "elppa"
    assert reverse("hello") == "olleh"
    assert reverse("Greetings!") == "!sgniteerG"
    assert reverse("abcd") == "dcba"
    assert reverse("  abcd") == "dcba  "
