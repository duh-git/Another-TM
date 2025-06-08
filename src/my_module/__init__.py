# determine which packages will be imported when using the "*" operator
__all__ = ["main", "func"]


# ** Best practices **
# makes your module easier to read for other developers
from .main import say_hi
from .func import fnc1, fnc2