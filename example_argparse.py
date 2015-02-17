#!/usr/bin/env python
"""Python example.

Basic Python example  with argparse.
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description='Basic Python example with argparse.')
    parser.add_argument('--foo', default='FOO', help='The foo parameter.')
    parser.add_argument('bar', help='The bar parameter.')
    args = parser.parse_args()

    # TODO: Do something more interesting here...
    print 'Hello there', args.foo, args.bar


if __name__ == '__main__':
    main()