Insertion Sort
==============

Use two lists, one ordered list and one unordered list. At the very start,
the ordered list is empty, and tne whole imput list is the unordered list.

In each step one number is taken from the unordered list, and the location
it belongs within the sorted list is found. This is done until the unordered
list is empty.

The algorithhm can be done in-place by dividing the input list in two. The
first item represents the ordered list, and the rest represent the ordered
list. Items from the right (ordered) side of the list are transferred to
left (unordered) side. This can be done by swapping list items or using
buffer variables.

More efficient in practice than most other simple quadratic sorting algorithms.

Time Complexity
---------------

- Best: `O(n)`
- Worst: `O(n^2)`
- Average: `O(n^2)`

Space Complexity
----------------

- Total: `O(n)`
- Auxiliary: `O(1)`

Resources
---------

- Insertion Sort at Wikipedia: https://en.wikipedia.org/wiki/Insertion_sort
- Insertion Sort at Rosetta Code: https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort
- Insertion Sort at Khan Academy: https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort
- Insertion Sort at freeCodeCamp: https://www.freecodecamp.org/news/insertion-sort-algorithm-example-in-java-and-c/
