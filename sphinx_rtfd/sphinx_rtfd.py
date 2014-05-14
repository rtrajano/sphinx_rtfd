#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module level docstring for the Greeter class"""

class Greeter():
    """A greeter class Greets people"""

    def __init__(self, msg, name):
        """Init func

        args:
          msg (str): a msg for the greeting
          name (str): someone to greet

        """
        self.msg = msg
        self.name = name

    def greet(self):
        """Greets a user.

        >>> my_greeter = Greeter('Hello', 'PUG')
        >>> my_greeter.greet()
        'Hello, PUG!'
        """
        return "{}, {}!".format(self.msg, self.name)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
