def find_gaps(intervals):
    # copy and sort the intervals
    # The default sorting behavior sorts by the first element in the tuple
    # note that intervals.sort() DOES NOT WORK (tuples are immutable)
    intervals = sorted(intervals)

    # will hold the gaps as they are found
    # to be converted to tuple at the end
    gaps = []
    
    # loop over each interval, comparing it to the next one
    # do not include the last interval because there is not a next one after it
    for i in range(len(intervals) - 1):
        current  = intervals[i]
        next = intervals[i+1]
        
        # if the end of the current interval is smaller than the 
        # start of the next one there is a gap that must be added
        if current[1] < next[0]:
            gaps.append((current[1], next[0]))

    # convert to tuple to match expected output types
    return tuple(gaps)


intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)
assert find_gaps(intervals_1) == ((10, 12), (15, 16), (25, 27))

intervals_2 = (
    (27, 30),
    (16, 20),
    (12, 15),
    (20, 25),
    (5, 10),
)
assert find_gaps(intervals_2) == ((10, 12), (15, 16), (25, 27))

intervals_3 = (
    (17, 35),
)
assert find_gaps(intervals_3) == tuple()

intervals_4 = (
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
)
assert find_gaps(intervals_4) == tuple()

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")
