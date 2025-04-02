#!/usr/bin/env python

import sys

current_word = None
current_count = 0

# Read input from standard input
for line in sys.stdin:
    # Split the line into word and count
    word, count = line.strip().split('\t', 1)
    
    # Convert count to integer
    try:
        count = int(count)
    except ValueError:
        # Skip malformed lines
        continue
    
    # If the word is the same as the previous one, increment the count
    if current_word == word:
        current_count += count
    else:
        # If we’ve switched words, output the previous word’s total
        if current_word:
            print(f"{current_word}\t{current_count}")
        # Start counting the new word
        current_word = word
        current_count = count

# Output the last word
if current_word:
    print(f"{current_word}\t{current_count}")