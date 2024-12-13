# gaps-problem
Problem to be completed during Industry Prep - Interview Prep activity time

## Problem Statement

Your goal is to write a function that finds gaps between given intervals.

The intervals will be an UNSORTED tuple containing tuples. Each inner tuple will represent an integer interval. It will have two elements: the first element is the beginning of the interval, the second element is the end of the interval. The first element is guaranteed to be strictly less than the second element.

Here is an example of an input tuple:

```py
intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)
```

For clarity of the example, this tuple is sorted. However, note that some of the other test cases are NOT SORTED.

In this example, we can see that the earliest interval ends at 10, and the next interval starts at 12. Thus, there is a gap from 10 to 12. Similarly, we can see there are two other gaps. Below is a tuple (in sorted order) showing all of the gaps for this example:

```py
expected_output = (
    (10, 12), 
    (15, 16), 
    (25, 27)
)
```

Note that there is NOT a gap at 20. One interval ends at 20, and another starts at 20. Though one interval may start at the same time another ends, you are guaranteed there will be no overlap between the input intervals.

Write a function that accepts the UNSORTED input intervals and returns a SORTED tuple of tuples containing all the gaps.

## Examples

### Example 1
```py
intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)

find_gaps(intervals_1)
```
Produces
```py
((10, 12), (15, 16), (25, 27))
```

### Example 2
```py
intervals_2 = (
    (27, 30),
    (16, 20),
    (12, 15),
    (20, 25),
    (5, 10),
)

find_gaps(intervals_2)
```
Produces
```py
((10, 12), (15, 16), (25, 27))
```

### Example 3
```py
intervals_3 = (
    (17, 35),
)

find_gaps(intervals_3)
```
Produces
```py
tuple()  # Empty tuple
```

### Example 4
```py
intervals_4 = (
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
)

find_gaps(intervals_4)
```
Produces
```py
tuple()  # Empty tuple
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if there is invalid input?
A: You can assume the input will be valid.

#### Q: What should I do if the input is an empty tuple?
A: You can assume there will be at least one interval present in the input.

#### Q: Do I have to worry about non-integers? (floats, complex, etc?)
A: You can assume the intervals will always be integers

#### Q: What should I do if there are no gaps?
A: Return an empty tuple (see last two test cases)

#### Q: What should I do if intervals overlap?
A: Though one interval may start at the same time another ends, you are guaranteed there will be no overlap between the input intervals. For example, there would NOT be intervals of (15, 21) and (20, 30)

#### Q: Will the input have a single interval with the same start and end? For example, (20, 20)
A: No.

#### Q: Can my output have a single interval with the same start and end? For example, (20, 20)
A: Also no.

#### Q: Does my output need to be sorted?
A: Yes.

#### Q: Is the input guaranteed to be sorted?
A: No.

### Hints

 - If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper

 - If they're struggling to sort the input tuple for more than a few minutes, suggest that they work on the rest of the problem and come back to sorting the input if they have time at the end. The first test case is already sorted, so they'll be able to test the rest of their logic.

- If they finish everything else and are still stuck on sorting the input, encourage search for how to sort a tuple in Python. If they're still stuck, you can just tell them to use `sorted`.

- If your candidate is returning a list and doesn't recognize why their code is not passing them the tests, ask them what the expected output types are.

- If your candidate struggles to make an empty tuple, you can tell them to use `tuple()`. If they struggle to make a tuple with a single element, you can tell them to use `(some_data,)`. Note the comma.

- If your candidate struggles to work with the outer tuple when constructing their gaps, you can encourage them to have the outer data structure to be a list to start and convert it to a tuple at the end (like the above example does).
