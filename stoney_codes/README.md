# Leetcode Problems

## Big O - Time and Space Complexity

**Time Complexity:** describes the amount of time necessary to execute an algorithm.

**Space Complexity:** describes the amount of memory or space utilized by an algorithm/program.

In computer science, big O notation is used to describe algorithms according to <em>how fast they run</em> (time complexity) or how much space they take (space complexity) <em>as the input size grows.</em>

**Technical definition: Big O** is a mathematical notation that describes the limiting behaviour of a function when the argument tends towards a particular value or infinity.

**Why do we need Big O?** Big O notation helps us understand how the performance of an algorithm changes as the size of the input grows, providing a simple way to compare and analyse different algorithms' efficiencies.

## Big O Reference Chart

<img src="./big-o-complexity-chart.png" width="400" />

## Big O Summary

| Time Complexity (fastest to slowest)  | Description | Example |
| --- | --- | --- |
| O(1) - Constant | Time taken remains constant regardless of input size. | Accessing an element in an array by index. |
| O(log N) - Logarithmic | Time taken increases logarithmically as the input size grows. Operations are typically halved at each step. Time increases linearly as N goes up exponentially. | Binary search in a sorted array. |
| O(N) - Linear | Time taken increases proportionally to the size of the input. If N doubles, time taken doubles. | Finding an item in an unsorted list. |
| O(N log N) - Linearithmic | Time taken increases in a linearithmic manner, often seen in `divide and conquer` algorithms. | Merge sort or quick sort |
| O(N^2) - Quadratic | Time taken increases quadratically as the input size grows. Each element needs to be compared to every other element (nested loops). | Bubble sort or selection sort. |
| O(2^N) - Exponential | Time taken doubles with each addition to N, leading to rapidly growing execution times. | Finding all subsets of a set. |
| O(N!) - Factorial | Time taken increases factorially with each increase in input size, leading to extremely slow execution times. | Solving the travelling salesman problem exhaustively. |

## Sections

1. Arrays
    - Contains duplicate &middot; <kbd>Easy</kbd>
    - Missing Number &middot; <kbd>Easy</kbd>
    - Find All Numbers Disappeared in a list &middot; <kbd>Easy</kbd>
    - Two Sum &middot; <kbd>Easy</kbd>
    - How Many Numbers Are Smaller Than the Current Number &middot; <kbd>Easy</kbd>
    - Minimum Time Visiting All Points &middot; <kbd>Easy</kbd>
    - Spiral Matrix &middot; <kbd>Medium</kbd>
    - Number of Islands

2. Arrays to Pointers
    - Best Time to Buy and Sell Stock
    - Squares of a Sorted Array
    - 3Sum
    - Longest Mountain in Array

3. Arrays Sliding Window
    - Contains Duplicate II
    - Minimum Absolute Difference
    - Minimum Size Subarray Sum

4. Bit Manipulation
    - Single Number

5. Dynamic Programming
    - Coin Change
    - Climbing Stairs
    - Maximum Subarray
    - Counting Bits
    - Range Sum Query - Immutable

6. Backtracking
    - Letter Case Permutation
    - Subsets
    - Combinations
    - Permutations

7. Linked Lists
    - Middle of Linked List
    - Linked List Cycle
    - Reverse Linked List
    - Remove Linked List Elements
    - Reverse Linked List II
    - Palindrome Linked List
    - Merge Two Sorted Lists

8. Stacks
    - Min Stack
    - Valid Parentheses
    - Evaluate Reverse Polish Notation
    - Stack Sorting

9. Queues
    - Implement Stack using Queues
    - Time Needed to Buy Tickets
    - Reverse the First K Elements of a Queue

10. Binary Trees
    - Average of Levels in Binary Tree
    - Minimum Depth of Binary Tree
    - Maximum Depth of Binary Tree
    - Min/Max Value Binary Tree
    - Binary Tree Level Order Traversal
    - Same Tree
    - Path Sum
    - Diameter of a Binary Tree
    - Invert Binary Tree
    - Lowest Common Ancestor of a Binary Tree

11. Binary Search Trees
    - Search in a Binary Search Tree
    - Insert into a Binary Search Tree
    - Convert Sorted Array to Binary Search Tree
    - Two Sum IV - Input is a BST
    - Lowest Common Ancestor of a Binary Search Tree
    - Minimum Absolute Difference in BST
    - Balance a Binary Search Tree
    - Delete Node in a BST
    - Kth Smallest Element in a BST

12. Heaps
    - Kth Largest Element in an Array
    - K Closest Points to Origin
    - Top K Frequent Elements
    - Task Scheduler

13. Graphs
    - Breadth and Depth First Traversal
    - Clone Graph
    - Core Graph Operations
    - Cheapest Flights Within K Stops
