#!/bin/bash

# Function to perform quick sort
quick_sort() {
    local arr=("$@")
    local n=${#arr[@]}

    if ((n < 2)); then
        echo "${arr[@]}"
        return
    fi

    local pivot=${arr[0]}
    local left=()
    local right=()

    for ((i=1; i<n; i++)); do
        if ((arr[i] <= pivot)); then
            left+=("${arr[i]}")
        else
            right+=("${arr[i]}")
        fi
    done

    # Recursive calls for left and right partitions
    local sorted_left=($(quick_sort "${left[@]}"))
    local sorted_right=($(quick_sort "${right[@]}"))

    echo "${sorted_left[@]} $pivot ${sorted_right[@]}"
}

# Read input from the user
read -p "Enter numbers separated by space: " -a arr

# Call the quick sort function
sorted_arr=($(quick_sort "${arr[@]}"))
echo "Sorted Array: ${sorted_arr[@]}"
