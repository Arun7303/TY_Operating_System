#!/bin/bash
echo "Enter a string:"
read str

# Convert lowercase to uppercase
upper=$(echo $str | tr 'a-z' 'A-Z')

# Convert uppercase to lowercase
lower=$(echo $str | tr 'A-Z' 'a-z')

echo "Uppercase: $upper"
