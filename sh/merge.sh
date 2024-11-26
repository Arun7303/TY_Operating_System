#!/bin/bash

# Function to merge two halves
merge() {
    local left=("${!1}")  # Left half
    local right=("${!2}") # Right half
    local merged=()       # Merged result
    local i=0 j=0

    # Merge the two halves
    while ((i < ${#left[@]} && j < ${#right[@]})); do
        if ((left[i] <= right[j])); then
            merged+=("${left[i]}")
            ((i++))
        else
            merged+=("${right[j]}")
            ((j++))
        fi
    done

    # Append remaining elements from both halves
    while ((i < ${#left[@]})); do
        merged+=("${left[i]}")
        ((i++))
    done
    while ((j < ${#right[@]})); do
        merged+=("${right[j]}")
        ((j++))
    done

    echo "${merged[@]}"
}

# Recursive merge sort function
merge_sort() {
    local arr=("$@")
    local n=${#arr[@]}
    if ((n < 2)); then
        echo "${arr[@]}"
        return
    fi

    local mid=$((n / 2))
    local left=("${arr[@]:0:mid}")
    local right=("${arr[@]:mid}")

    # Recursive calls for left and right halves
    local sorted_left=($(merge_sort "${left[@]}"))
    local sorted_right=($(merge_sort "${right[@]}"))

    # Merge sorted halves
    merge sorted_left[@] sorted_right[@]
}

# Read input from the user
read -p "Enter numbers separated by space: " -a arr

# Call the merge sort function
sorted_arr=($(merge_sort "${arr[@]}"))
echo "Sorted Array: ${sorted_arr[@]}"
