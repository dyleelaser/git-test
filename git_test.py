# Here, define function
def hello(name: str):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    print(f"Hello, {name}!")

# This is timetravel time.
#print("Hello, Timekeeper.")
hello("Timekeeper")
hello(123)

