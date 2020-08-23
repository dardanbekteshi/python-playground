import time
from typing import Generator

def slow_func(seconds:int) -> str:
    print(f"sleeping {seconds} seconds")
    time.sleep(seconds)
    return "slow"

def lazy_func(seconds:int) -> Generator[str, None, None]:
    print(f"sleeping {seconds} seconds")
    time.sleep(seconds)
    yield "lazy"

var1 = lazy_func(4)
sleep = False
if sleep:
    next(var1)
else:
    print("no sleeping, this was a lazy evaluation...")

var2 = slow_func(3)
sleep = False
if sleep:
    print(var2)
else:
    print("there was sleeping even though it was not needed")