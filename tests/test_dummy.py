from dummyapp.package import first
from dummyapp.package.sub_package import second
from dummyapp import async_stuff

def test_first():
    first.print_stuff()

def test_second():
    second.print_stuff()

def test_mix():
    second.print_from_parent()

def test_slow_it():
    original_url = "https://jsonplaceholder.typicode.com/todos/11"
    delay = 5
    slow_url = async_stuff.slow_it(original_url=original_url,delay=delay)
    assert slow_url == "http://slowwly.robertomurray.co.uk/delay/5000/url/https://jsonplaceholder.typicode.com/todos/11"