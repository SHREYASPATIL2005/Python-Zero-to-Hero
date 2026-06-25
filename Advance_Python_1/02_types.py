from typing import List, Dict, Tuple, Set, Union

n : int = 5

name: str = "Shreyas"

def sum(a: int, b: int) -> int:
    return a + b

sum(1, 2)

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union - variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 123  # Now it can also hold an integer