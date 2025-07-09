# test_git_test.py
from src.git_test import hello

def test_hello_prints_correctly(capfd):
    hello("Testuser")
    out, err = capfd.readouterr()
    assert "Hello, Testuser" in out