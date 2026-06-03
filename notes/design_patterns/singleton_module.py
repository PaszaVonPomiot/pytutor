"""
Module-level singleton.

Python imports a module once per interpreter process and stores it in
`sys.modules`. Later imports return the cached module object, so module-level
state is shared by all importers.

This is the simplest singleton in Python: create one object at module import
time and import that object wherever it is needed.
"""

from dataclasses import dataclass


@dataclass
class Config:
    value: int = 42


config = Config()
