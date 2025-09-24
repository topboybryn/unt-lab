#!/usr/bin/env python3
"""
Python Programming Assignment Solutions
=======================================

This file contains comprehensive solutions for all 7 programming tasks.
Each task is clearly sectioned with examples and test cases.

Author: Created for UNT Lab Assignment
Date: 2024
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Union


# =============================================================================
# TASK 1: String Variable and Output
# =============================================================================

def task1_string_output():
    """
    Create a string variable and print an output statement utilizing that variable.
    """
    print("=== TASK 1: String Variable and Output ===")
    
    # Create a string variable
    greeting_message = "Welcome to the Python Programming Solutions!"
    
    # Print output statement utilizing the variable
    print(f"Output: {greeting_message}")
    print(f"The length of our message is: {len(greeting_message)} characters")
    print(f"Message in uppercase: {greeting_message.upper()}")
    print()


# =============================================================================
# TASK 2: FizzBuzz Problem
# =============================================================================

def fizzbuzz(n: int = 100) -> None:
    """
    Print numbers from 1 to n with FizzBuzz rules:
    - For multiples of 3, print "Fizz"
    - For multiples of 5, print "Buzz" 
    - For multiples of both 3 and 5, print "FizzBuzz"
    
    Args:
        n: Upper limit for the range (default: 100)
    """
    print(f"=== TASK 2: FizzBuzz Problem (1 to {n}) ===")
    
    for i in range(1, n + 1):
        if i % 15 == 0:  # Multiple of both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Multiple of 3
            print("Fizz")
        elif i % 5 == 0:  # Multiple of 5
            print("Buzz")
        else:
            print(i)
    print()


def fizzbuzz_compact(n: int = 100) -> List[str]:
    """
    Compact version of FizzBuzz that returns a list of results.
    
    Args:
        n: Upper limit for the range (default: 100)
        
    Returns:
        List of FizzBuzz results
    """
    return [
        "FizzBuzz" if i % 15 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        str(i)
        for i in range(1, n + 1)
    ]


# =============================================================================
# TASK 3: Basic Mathematical Operations
# =============================================================================

def mathematical_operations(a: Union[int, float], b: Union[int, float]) -> Tuple[float, float, float]:
    """
    Calculate the sum, difference, and product of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Tuple containing (sum, difference, product)
    """
    sum_result = a + b
    difference = a - b
    product = a * b
    
    return sum_result, difference, product


def task3_mathematical_operations():
    """
    Demonstrate basic mathematical operations with example variables.
    """
    print("=== TASK 3: Basic Mathematical Operations ===")
    
    # Create two numerical variables
    num1 = 15.5
    num2 = 7.3
    
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    
    # Calculate operations
    sum_result, difference, product = mathematical_operations(num1, num2)
    
    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference}")
    print(f"Product: {num1} × {num2} = {product}")
    
    # Additional operations
    if num2 != 0:
        quotient = num1 / num2
        print(f"Quotient: {num1} ÷ {num2} = {quotient:.4f}")
    
    print()


# =============================================================================
# TASK 4: Matrix Operations
# =============================================================================

def matrix_dot_product_transpose(matrix: np.ndarray) -> np.ndarray:
    """
    Calculate the dot product of a matrix and its transpose.
    
    Args:
        matrix: Input matrix (numpy array)
        
    Returns:
        Result of matrix × matrix^T
    """
    transpose = matrix.T
    result = np.dot(matrix, transpose)
    return result


def task4_matrix_operations():
    """
    Demonstrate matrix operations with dot product and transpose.
    """
    print("=== TASK 4: Matrix Operations ===")
    
    # Create a sample matrix
    original_matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print("Original Matrix:")
    print(original_matrix)
    
    print("\nTranspose of the Matrix:")
    transpose = original_matrix.T
    print(transpose)
    
    print("\nDot Product of Matrix and its Transpose:")
    result = matrix_dot_product_transpose(original_matrix)
    print(result)
    
    # Additional example with rectangular matrix
    rect_matrix = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ])
    
    print(f"\nRectangular Matrix ({rect_matrix.shape}):")
    print(rect_matrix)
    
    print(f"\nDot Product Result Shape: {matrix_dot_product_transpose(rect_matrix).shape}")
    print(matrix_dot_product_transpose(rect_matrix))
    print()


# =============================================================================
# TASK 5: Factorial Functions
# =============================================================================

def factorial_recursive(n: int) -> int:
    """
    Calculate factorial using recursion.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial using iteration.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def task5_factorial_functions():
    """
    Demonstrate both recursive and iterative factorial implementations.
    """
    print("=== TASK 5: Factorial Functions ===")
    
    test_numbers = [0, 1, 5, 7, 10]
    
    print("Comparing Recursive vs Iterative Factorial:")
    print("-" * 50)
    print(f"{'n':<3} {'Recursive':<12} {'Iterative':<12} {'Match':<8}")
    print("-" * 50)
    
    for n in test_numbers:
        recursive_result = factorial_recursive(n)
        iterative_result = factorial_iterative(n)
        match = "✓" if recursive_result == iterative_result else "✗"
        
        print(f"{n:<3} {recursive_result:<12} {iterative_result:<12} {match:<8}")
    
    print("\nTesting larger numbers (iterative only for efficiency):")
    for n in [15, 20]:
        result = factorial_iterative(n)
        print(f"{n}! = {result:,}")
    
    print()


# =============================================================================
# TASK 6: Anagram Checker
# =============================================================================

def is_anagram(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.
    
    Args:
        word1: First word
        word2: Second word
        
    Returns:
        True if words are anagrams, False otherwise
    """
    # Convert to lowercase and remove spaces
    clean_word1 = word1.lower().replace(" ", "")
    clean_word2 = word2.lower().replace(" ", "")
    
    # Check if lengths are different
    if len(clean_word1) != len(clean_word2):
        return False
    
    # Sort characters and compare
    return sorted(clean_word1) == sorted(clean_word2)


def is_anagram_frequency(word1: str, word2: str) -> bool:
    """
    Alternative anagram checker using character frequency counting.
    
    Args:
        word1: First word
        word2: Second word
        
    Returns:
        True if words are anagrams, False otherwise
    """
    # Convert to lowercase and remove spaces
    clean_word1 = word1.lower().replace(" ", "")
    clean_word2 = word2.lower().replace(" ", "")
    
    # Check if lengths are different
    if len(clean_word1) != len(clean_word2):
        return False
    
    # Count character frequencies
    char_count = {}
    
    # Count characters in first word
    for char in clean_word1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract character counts from second word
    for char in clean_word2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    # Check if all counts are zero
    return all(count == 0 for count in char_count.values())


def task6_anagram_checker():
    """
    Demonstrate anagram checking with various test cases.
    """
    print("=== TASK 6: Anagram Checker ===")
    
    test_cases = [
        ("listen", "silent"),
        ("elbow", "below"),
        ("study", "dusty"),
        ("hello", "world"),
        ("dormitory", "dirty room"),
        ("conversation", "voices rant on"),
        ("astronomer", "moon starer"),
        ("python", "java"),
        ("race", "care"),
        ("evil", "vile")
    ]
    
    print("Testing anagram pairs:")
    print("-" * 60)
    print(f"{'Word 1':<15} {'Word 2':<15} {'Sorting':<10} {'Frequency':<10}")
    print("-" * 60)
    
    for word1, word2 in test_cases:
        result_sort = is_anagram(word1, word2)
        result_freq = is_anagram_frequency(word1, word2)
        
        sort_symbol = "✓" if result_sort else "✗"
        freq_symbol = "✓" if result_freq else "✗"
        
        print(f"{word1:<15} {word2:<15} {sort_symbol:<10} {freq_symbol:<10}")
    
    print()


# =============================================================================
# TASK 7: Mathematical Function Plotting
# =============================================================================

def plot_mathematical_function():
    """
    Plot a simple mathematical function using matplotlib.
    Creates multiple subplots showing different mathematical functions.
    """
    print("=== TASK 7: Mathematical Function Plotting ===")
    
    # Create x values
    x = np.linspace(-10, 10, 1000)
    
    # Create figure with subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Mathematical Function Plotting', fontsize=16, fontweight='bold')
    
    # Plot 1: Quadratic function
    y1 = x**2
    ax1.plot(x, y1, 'b-', linewidth=2, label='y = x²')
    ax1.set_title('Quadratic Function')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Plot 2: Sine and Cosine functions
    y2_sin = np.sin(x)
    y2_cos = np.cos(x)
    ax2.plot(x, y2_sin, 'r-', linewidth=2, label='y = sin(x)')
    ax2.plot(x, y2_cos, 'g-', linewidth=2, label='y = cos(x)')
    ax2.set_title('Trigonometric Functions')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xlim(-2*np.pi, 2*np.pi)
    
    # Plot 3: Exponential function
    x3 = np.linspace(-3, 3, 1000)
    y3 = np.exp(x3)
    ax3.plot(x3, y3, 'm-', linewidth=2, label='y = eˣ')
    ax3.set_title('Exponential Function')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    ax3.set_ylim(0, 20)
    
    # Plot 4: Polynomial function
    y4 = x**3 - 3*x**2 + 2*x + 1
    ax4.plot(x, y4, 'orange', linewidth=2, label='y = x³ - 3x² + 2x + 1')
    ax4.set_title('Cubic Polynomial')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    ax4.set_xlim(-2, 4)
    ax4.set_ylim(-10, 10)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('/home/runner/work/unt-lab/unt-lab/mathematical_functions_plot.png', 
                dpi=300, bbox_inches='tight')
    
    print("Mathematical functions plotted and saved as 'mathematical_functions_plot.png'")
    print("The plot includes:")
    print("- Quadratic function: y = x²")
    print("- Trigonometric functions: y = sin(x) and y = cos(x)")
    print("- Exponential function: y = eˣ")
    print("- Cubic polynomial: y = x³ - 3x² + 2x + 1")
    print()
    
    # Show the plot (commented out for non-interactive environment)
    # plt.show()


# =============================================================================
# MAIN EXECUTION AND TESTING
# =============================================================================

def run_all_tasks():
    """
    Execute all tasks with their examples and test cases.
    """
    print("PYTHON PROGRAMMING ASSIGNMENT SOLUTIONS")
    print("=" * 80)
    print()
    
    # Execute all tasks
    task1_string_output()
    fizzbuzz(20)  # Show first 20 for brevity
    task3_mathematical_operations()
    task4_matrix_operations()
    task5_factorial_functions()
    task6_anagram_checker()
    plot_mathematical_function()
    
    print("=" * 80)
    print("ALL TASKS COMPLETED SUCCESSFULLY!")
    print("=" * 80)


def test_functions():
    """
    Run comprehensive tests for all functions.
    """
    print("RUNNING COMPREHENSIVE TESTS")
    print("=" * 50)
    
    # Test mathematical operations
    assert mathematical_operations(5, 3) == (8, 2, 15)
    assert mathematical_operations(10.5, 2.5) == (13.0, 8.0, 26.25)
    print("✓ Mathematical operations tests passed")
    
    # Test factorial functions
    for n in range(6):
        assert factorial_recursive(n) == factorial_iterative(n)
    assert factorial_recursive(5) == 120
    assert factorial_iterative(0) == 1
    print("✓ Factorial function tests passed")
    
    # Test anagram checker
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "world") == False
    assert is_anagram_frequency("evil", "vile") == True
    assert is_anagram_frequency("python", "java") == False
    print("✓ Anagram checker tests passed")
    
    # Test FizzBuzz
    fizz_result = fizzbuzz_compact(15)
    assert fizz_result[2] == "Fizz"  # 3rd element (index 2) should be "Fizz"
    assert fizz_result[4] == "Buzz"  # 5th element (index 4) should be "Buzz"
    assert fizz_result[14] == "FizzBuzz"  # 15th element should be "FizzBuzz"
    print("✓ FizzBuzz tests passed")
    
    # Test matrix operations
    test_matrix = np.array([[1, 2], [3, 4]])
    result = matrix_dot_product_transpose(test_matrix)
    expected_shape = (2, 2)
    assert result.shape == expected_shape
    print("✓ Matrix operations tests passed")
    
    print("=" * 50)
    print("ALL TESTS PASSED SUCCESSFULLY!")
    print("=" * 50)


if __name__ == "__main__":
    # Run tests first
    test_functions()
    print()
    
    # Run all task demonstrations
    run_all_tasks()