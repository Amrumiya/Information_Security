#!/bin/bash

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file> <word>"
    exit 1
fi

file=$1
word=$2

# Check if file exists
if [ ! -f "$file" ]; then
    echo "Error: File not found!"
    exit 1
fi

# Count occurrences of the word (case-insensitive)
count=$(grep -o -i "$word" "$file" | wc -l)

echo "The word '$word' appears $count times in $file."
