#!/usr/bin/env python
"""Python example.

Basic Python example.
"""

import sys


def main():
    # TODO: Do something more interesting here...
    print __doc__
    print 'Hello there from', sys.argv[0]
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself


if __name__ == '__main__':
    main()