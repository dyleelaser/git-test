# src/git_test.py

# imports
import sys
from datetime import datetime

# Here, define function
def hello(name: str):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, {name}! It's [{now}]")

# This is timetravel time.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        hello(sys.argv[1])
    else:
        print("Usage: python git_test.py <name>")