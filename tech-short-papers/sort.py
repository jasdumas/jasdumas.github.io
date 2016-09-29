'''
quick sorting algorithm
https://en.wikipedia.org/wiki/Sorting_algorithm
http://stackoverflow.com/questions/70402/why-is-quicksort-better-than-mergesort
'''

def sort(array):
    
    """ Quick Sort a list """
    # 3-way partition of the list
    less = [] # bucket list to capture values less than the pivot
    equal = [] # bucket list to capture values equal to the pivot
    greater = [] # bucket list to capture values greater than the pivot

    if len(array) > 1: # as long as we have a list larger than 1 (one value)
        pivot = array[0] # our pivot point for comparison
        for x in array: # for each value in the array
            if x < pivot:
                less.append(x) # append to a separate list
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something! - which recursively calls our sort function back on our new lists
        return sort(less)+ equal + sort(greater)  # Just use the + operator to join lists
        print(sort(less)+ equal + sort(greater))
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

    
array=[12,4,5,6,7,3,1,15]
print(sort(array))

