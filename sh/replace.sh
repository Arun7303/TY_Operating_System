#!/bin/bash
echo "Enter the file name:"
read file
total_lines=$(wc -l < "$file")
lines_to_replace=$((total_lines / 5))
for i in $(seq 1 $lines_to_replace); do
    line_num=$(shuf -i 1-$total_lines -n 1)
    sed -i "${line_num}s/.*/REPLACED LINE/" "$file"
done
echo "$lines_to_replace lines have been replaced with 'REPLACED LINE'."

