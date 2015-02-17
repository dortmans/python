#!/usr/bin/env python
"""Python example.

YAML to JSON.
"""

import os, argparse, yaml, json


def yaml_to_json(yaml_file, compressed):
    data = yaml.load(open(yaml_file, 'r'))
    if compressed:
        separators = (',', ':')
        indent = None
    else:
        separators = None
        indent = 2
    json_file = os.path.splitext(yaml_file)[0] + '.json'
    json.dump(data, file(json_file, 'w'), separators=separators, indent=indent)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read .yaml file and write equivalent .json file')
    parser.add_argument('-c', '--c', action='store_true', help='compressed json output')
    parser.add_argument('yaml_file', help='The .yaml file to convert')
    args = parser.parse_args()
    yaml_to_json(args.yaml_file, args.c)
