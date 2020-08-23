from dummyapp.package import first

def print_stuff():
    print("Hello from second")

def print_from_parent():
    print("I am in second")
    first.print_stuff()
