#!/usr/bin/env python3

import sys
import yaml
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', help = 'input file')
parser.add_argument('--output', '-o', required = True, help = 'output file')
args = parser.parse_args()

with open(sys.argv[1], 'r') as file:
    data = yaml.safe_load(file);
    with open(args.output, 'w') as output:
        output.write('/**/\nnews(')
        json.dump(data, output, indent=4)
        output.write(');')
