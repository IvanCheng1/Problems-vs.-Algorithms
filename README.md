# Data Structures and Algorithms Project
* Consists of seven mini projects
### Table of content
* [Finding the Square Root of an Integer](#problem-1---finding-the-square-root-of-an-integer)
* [Search in a Rotated Sorted Array](#Problem-2---Search-in-a-Rotated-Sorted-Array)
* [Rearrange Array Elements](##Problem-3---Rearrange-Array-Elements)
* [Dutch National Flag Problem](##Problem-4---Dutch-National-Flag-Problem)
* [Building a Trie in Python](#Problem-5---Building-a-Trie-in-Python)
* [Max and Min in a Unsorted Array](#Problem-6---Max-and-Min-in-a-Unsorted-Array)
* [HTTPRouter using a Trie](#Problem-7---HTTPRouter-using-a-Trie)

#### Problem 1 - Finding the Square Root of an Integer
* Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
* For example if the given number is 16, then the answer would be 4.
* If the given number is 27, the answer would be 5 because `sqrt(5) = 5.196` whose floor value is 5.

#### Problem 2 - Search in a Rotated Sorted Array
* You are given a sorted array which is rotated at some random pivot point.
* Example: `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`
* You are given a target value to search. If found in the array return its index, otherwise return -1.
* You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

> Example:
> Input: `nums = [4,5,6,7,0,1,2], target = 0, Output: 4`

#### Problem 3 - Rearrange Array Elements
* Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.
* for e.g. `[1, 2, 3, 4, 5]`
* The expected answer would be `[531, 42]`. Another expected answer can be `[542, 31]`. In scenarios such as these when there are more than one possible answers, return any one.

#### Problem 4 - Dutch National Flag Problem
* Given an input array consisting on only 0, 1, and 2, sort the array in a *single traversal*. You're not allowed to use any sorting function that Python provides.

#### Problem 5 - Building a Trie in Python
* Use a Trie to build a autocomplete function.

#### Problem 6 - Max and Min in a Unsorted Array
* In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
* **Bonus Challenge**: find the max and min in a single traversal.

#### Problem 7 - HTTPRouter using a Trie
* Implementing a HTTPRouter using a Trie data structure.
* The Trie will contain a part of the http path at each node, building from the root node `/`
* In addition to a path, a handler is added at a node, for the sake of simplicity
