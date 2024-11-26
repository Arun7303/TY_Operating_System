#!/bin/bash

# Read the array of numbers
echo "Enter numbers separated by spaces:"
read -a arr

# Get the length of the array
n=${#arr[@]}

# Bubble Sort algorithm
for ((i = 0; i < n-1; i++)); do
    for ((j = 0; j < n-i-1; j++)); do
        if ((arr[j] > arr[j+1])); then
            # Swap arr[j] and arr[j+1]
            temp=${arr[j]}
            arr[j]=${arr[j+1]}
            arr[j+1]=$temp
        fi
    done
done

# Output the sorted array
echo "Sorted array:"
echo "${arr[@]}"
