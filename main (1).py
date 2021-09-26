"""
Instructions:
1. Create a class named ReversedString that inherits from StringOperations class
2. Implement the function reverse
3. reverse function should be a one liner function that returns the reverse string to_be_reversed
4. Instantiate the class ReversedString
5. Print to show your function implementation result
"""


class StringOperations:
    def reverse(self, *, to_be_reversed: str = None): 
        raise NotImplementedError

# ---- class inherits from StringOperations class:  ----

class ReversedString(StringOperations):
    def reverse(self, *, to_be_reversed: str = None):
        return to_be_reversed[::-1]

# ---- Instantiate the class ReversedString: ----

var1 = ReversedString()

# ---- Print to show the function implementation result: ----

print(var1.reverse(to_be_reversed="Hi, i'm Dena!"))