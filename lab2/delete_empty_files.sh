#!/bin/bash

# Check if a directory is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory=$1

# Check if directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory not found!"
    exit 1
fi

# Find empty files
empty_files=$(find "$directory" -type f -size 0)

if [ -z "$empty_files" ]; then
    echo "No empty files found."
else
    echo "Deleting the following empty files:"
    echo "$empty_files"
    rm $empty_files
    echo "Deletion complete."
fi
