import os
from contextlib import suppress

# Deleting file that may not exist
try:
    os.remove("somefile.tmp")
except FileNotFoundError:
    pass

# Equivalent to:
with suppress(FileNotFoundError):
    os.remove("somefile.tmp")

# --------------------------------------------------

# Suppress multiple exceptions
with suppress(FileNotFoundError, PermissionError):
    os.remove("somefile.tmp")

# Equivalent to:
try:
    os.remove("somefile.tmp")
except (FileNotFoundError, PermissionError):
    pass

# --------------------------------------------------

# Suppress all exceptions
with suppress(Exception):
    os.remove("somefile.tmp")

# --------------------------------------------------

# Removing key from dictionary
d = {"a": 1}
with suppress(KeyError):
    del d["b"]

# --------------------------------------------------

# Nested try-except blocks
try:
    ...
    try:
        ...
    except ...:
        pass
except ...:
    pass

# Equivalent to:
with suppress(...):
    ...
    with suppress(...):
        ...
