#!/bin/bash

echo "Enter first number: "
read num1

echo "Enter second number: "
read num2

echo "Choose operation (+, -, /, *): "
read ope

# Perform operations based on the chosen operator
if [ "$ope" == "+" ]; then
    res=$((num1 + num2))
elif [ "$ope" == "-" ]; then
    res=$((num1 - num2))
elif [ "$ope" == "/" ]; then
    if [ "$num2" -eq 0 ]; then
        echo "Division by zero is not allowed."
        exit 1
    fi
    res=$((num1 / num2))
elif [ "$ope" == "*" ]; then
    res=$((num1 * num2))
else
    echo "Invalid operation. Please choose +, -, /, or *."
    exit 1
fi

echo "The result is: $res"

