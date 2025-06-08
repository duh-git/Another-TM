# PROBLEM SOLVED

# OUTPUT:
# Function 1
# Function 2
# Hi!       
# Hi!

# Modules problem
# Here is different ways to import staff from your module
# NOTICE: your module should be placed in your main app folder which using it.
#         In order for your module to be a child of your main app

from my_module.func import fnc1
fnc1()

from my_module import *
func.fnc2()
main.say_hi()

from my_module.main import say_hi
say_hi()

# etc