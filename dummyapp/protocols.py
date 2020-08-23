from typing import Protocol, Iterable

class Printable(Protocol):
    def print(self) -> None: 
        ...

class Document(Printable):
    def print(self):
        print("Hello world from Document")

class Photo(Printable):
    def print(self) -> None:
        print("Hello world from Photo")

class Money(): # No need for explicit "inheritance" from Printable
    def print(self) -> None:
        print("Hello world from Money")


def print_many(*args: Printable) -> None:
    for p in args:
        p.print()

print_many(Document(), Photo(), Money())

print_many(Document())