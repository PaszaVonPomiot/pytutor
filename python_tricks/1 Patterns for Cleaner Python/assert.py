"""
Covering Your A** With Assertions

Python’s assert statement is a debugging aid that tests a condition as an internal self-check in your program.
Asserts should only be used to help developers identify bugs.
They’re not a mechanism for handling run-time errors.
Asserts can be globally disabled with an interpreter setting.

Use only for unrecoverable errors and for debug purposes, not as main app logic.
Assert works only if global variable __debug__ = True.
Assert is skipped for -O, -OO switches or PYTHONOPTIMIZE env variable.

Don't used assert for code that should never be skipped.
"""

assert 1 > 2, "AssertionError: should show up"
