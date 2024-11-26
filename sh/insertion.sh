#!/bin/bash

# Function to perform insertion sort
insertion_sort() {
    arr=("$@")  # Array of numbers passed as arguments
    n=${#arr[@]}  # Number of elements in the array

    for ((i=1; i<n; i++)); do
        key=${arr[i]}
        j=$((i-1))

        # Move elements that are greater than the key one position ahead
        while ((j >= 0 && arr[j] > key)); do
            arr[j+1]=${arr[j]}
            j=$((j-1))
        done

        # Place the key in its correct position
        arr[j+1]=$key
    done

    # Print the sorted array
    echo "Sorted Array: ${arr[@]}"
}

# Read input from the user
read -p "Enter numbers separated by space: " -a arr

# Call the function
insertion_sort "${arr[@]}"
