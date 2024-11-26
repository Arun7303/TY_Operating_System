#!/bin/bash

# Prompt the user for input
read -p "Enter a string: " input

# Initialize variables
length=${#input}
reversed=""

# Reverse the string manually
for (( i=length-1; i>=0; i-- )); do
    reversed="$reversed${input:i:1}"
done

# Output the reversed string
echo "Reversed string: $reversed"
