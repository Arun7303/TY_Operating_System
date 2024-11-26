#!/bin/bash

# Read the input string
echo "Enter a string:"
read str

# Reverse the string
rev_str=$(echo "$str" | rev)

# Check if the string is equal to its reverse
if [ "$str" = "$rev_str" ]; then
    echo "The string is a palindrome."
else
    echo "The string is not a palindrome."
fi

