#!/usr/bin/env python
"""Hello World in Python

Example use of Class
"""


class Example(object):
    def __init__(self, message):
        """Constructor
        """
        print "<constructor>"
        self.message = message

    def __del__(self):
        """Destructor
        """
        print "<destructor>"

    def run(self):
        print self.message


if __name__ == '__main__':
    example = Example("Hello, world!")
    example.run()