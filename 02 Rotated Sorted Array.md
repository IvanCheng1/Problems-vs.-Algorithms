# Search in a Rotated Sorted Array

* You are given a sorted array which is rotated at some random pivot point.
* Example: `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`
* You are given a target value to search. If found in the array return its index, otherwise return -1.
* You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

Example:
Input: `nums = [4,5,6,7,0,1,2], target = 0, Output: 4`

### Explanation
* Used divide & conquer to have a time efficiency of O(log(n))
* the input size is halved every time it recurs
* recur until number is found, else return `-1`

### Time efficiency
* O(log(n))
* searching in and halving every time

### Space efficiency
* O(n)
