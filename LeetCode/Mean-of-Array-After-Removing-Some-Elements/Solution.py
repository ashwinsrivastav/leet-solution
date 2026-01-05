Determine the number of elements to remove: We need to remove a certain percentage of elements from both ends of the sorted array. This percentage is given as 5% in the problem statement. We calculate the number of elements to remove (numToRemove) as (5×n)/100(5×n)/100, where nn is the size of the array.

Calculate the trimmed mean:
    We iterate over the array starting from the numToRemove-th element and ending at the (n−numToRemove)(n−numToRemove)-th element. These elements form the middle range of the sorted array after removing elements from both ends.
    We sum up the values of the elements within this middle range.
    We calculate the mean of the middle range by dividing the sum by the number of elements remaining after trimming both ends, which is (n−2×numToRemove)(n−2×numToRemove).

Return the trimmed mean: The calculated mean is returned as the result.