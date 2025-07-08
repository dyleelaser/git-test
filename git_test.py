# imports
from datetime import datetime

# Here, define function
def hello(name: str):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, {name}! It's [{now}]")

# This is timetravel time.
#print("Hello, Timekeeper.")
#hello(123)
hello("Timekeeper")

