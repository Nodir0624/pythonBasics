# Functions execution file
# module, package, import
# ./src/functions/functions.py  -> greet_user_by_name()
# from src.functions.functions import greet_user_by_name, thank_you_by_name, greet_user
from src.functions.functions import *
from src.functions.functions_return import *

# import line reads and executes the files




print("# EXECUTION: *************")
greet_user_by_name('john')
greet_user()
greet_user_by_name('jane')
greet_user()
greet_user_by_name('britney')
thank_you_by_name('john', 10)
thank_you_by_name('jane', 5)
thank_you_by_name('britney', 20)
thank_you_by_name('mark', 1)

print("Executing the functions with Positional Arguments.")
print(get_full_name('john', 'doe'))  # third argument is optional
print(get_full_name('john', 'doe', 'brown'))
# arguments you pass are positional, which will be assigned to each parameter based on position you enter

print("Executing the functions with Keyword Arguments (not Positional Arguments).")
print(get_full_name(fistname='jane', middlename='rogers', lastname='doe'))
print(get_full_name('anne', 'doe', 'marie'))
print(get_full_name(456, 'asdf', 000))

