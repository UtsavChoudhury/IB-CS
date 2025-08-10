# False
# Boolean value representing false.

# None
# Represents the absence of a value or a null value.

# True
# Boolean value representing true.

# and
# Logical AND operator, returns True if both operands are true.

# as 
# Used to create an alias (e.g., in imports, exception handling, or with statements).

# assert 
# Used for debugging, tests if a condition is true, raises an AssertionError if false.

assert 2 + 2 == 4  # passes silently
# assert 2 + 2 == 5  # raises AssertionError (uncomment to test)


# async
# Defines an asynchronous function.

import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("World!")


# await
# Used inside async functions to pause until an awaitable completes.

async def main():
    await say_hello()

# To run async example:
# asyncio.run(main())


# break
# Exits the nearest enclosing loop immediately.

# class
# Defines a new user-defined class.

# continue
# Skips the rest of the current loop iteration and proceeds to the next iteration.

# def
# Defines a new function or method.

# del
# Deletes a variable, list item, dictionary entry, or object attribute.

x = 10
del x
# print(x)  # NameError: x no longer exists

lst = [1, 2, 3]
del lst[1]  # lst becomes [1, 3]
print(lst)

d = {'a': 1, 'b': 2}
del d['a']  # d becomes {'b': 2}
print(d)


# elif
# Short for "else if," used in conditional statements after if.

# else
# Defines a block of code to execute if preceding conditions are false.

# except
# Catches exceptions in a try-except block.

# finally
# Defines a block of code that always runs after try-except, regardless of exceptions.

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Caught division by zero")
finally:
    print("This always runs")


# for
# Starts a for-loop, iterating over items in a sequence.

# from
# Imports specific parts from a module.

# global
# Declares that a variable inside a function is global (outside function scope).

# if
# Starts a conditional statement.

# import
# Imports a module.

# in
# Tests membership (if an item is in a sequence) or used in loops to iterate.

# is
# Tests object identity (if two references point to the same object).

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True (same object)
print(a is c)  # False (different objects)


# lambda
# Creates an anonymous (unnamed) function.

square = lambda x: x * x
print(square(5))  # Output: 25


# nonlocal
# Declares that a variable refers to the nearest enclosing (non-global) scope.

def outer():
    x = "hello"
    def inner():
        nonlocal x
        x = "world"
    inner()
    print(x)

outer()  # prints "world"


# not
# Logical NOT operator, negates a boolean value.

# or
# Logical OR operator, returns True if at least one operand is true.

# pass
# Does nothing; a placeholder statement.

# raise
# Raises an exception.

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# divide(10, 0)  # Uncomment to raise ValueError


# return
# Exits a function and optionally passes back a value.

# try
# Defines a block to test for exceptions.

# while 
# Starts a while-loop, repeating as long as a condition is true.
