# Finding the Square Root of an Integer

* Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
* For example if the given number is 16, then the answer would be 4.
* If the given number is 27, the answer would be 5 because `sqrt(5) = 5.196` whose floor value is 5.

### Explanation
* Used divide & conquer to have a time efficiency of O(log(n))
* the input size is halved every time it recurs
* returns `mid` when the square number is between `mid` and `mid + 1` as that's the floor value

### Time efficiency
* O(log(n))
* halving the size every time

### Space efficiency
* O(1)
