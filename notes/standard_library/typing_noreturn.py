from typing import NoReturn


# annotating function that never returns
def stop() -> NoReturn:
    raise Exception("no way")
