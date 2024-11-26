#!/bin/bash

# Function to perform selection sort
selection_sort() {
    arr=("$@")  # Array of numbers passed as arguments
    n=${#arr[@]}  # Number of elements in the array

    for ((i=0; i<n-1; i++)); do
        min_idx=$i
        for ((j=i+1; j<n; j++)); do
            if [ "${arr[j]}" -lt "${arr[min_idx]}" ]; then
                min_idx=$j
            fi
        done
        # Swap elements
        if [ $min_idx -ne $i ]; then
            temp=${arr[i]}
            arr[i]=${arr[min_idx]}
            arr[min_idx]=$temp
        fi
    done

    # Print the sorted array
    echo "Sorted Array: ${arr[@]}"
}

# Read input from the user
read -p "Enter numbers separated by space: " -a arr

# Call the function
selection_sort "${arr[@]}"
