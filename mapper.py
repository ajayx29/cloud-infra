#!/usr/bin/env python

import sys

# Read input from standard input
for line in sys.stdin:
    # Remove leading/trailing whitespace and split into words
    words = line.strip().split()
    # Emit each word with a count of 1
    for word in words:
        print(f"{word}\t1")