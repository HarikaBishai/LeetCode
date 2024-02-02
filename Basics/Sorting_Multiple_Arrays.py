# Sort first array and sort second array based on the first array sorted positions

arr1 = [10, 8, 0, 5, 3]
arr2 = [2, 4, 1, 1, 3]

# Zip the two arrays
combined_arr  = list(zip(arr1, arr2))

# Now sort the combined array
arr1_wise_sort = sorted(combined_arr)
arr2_wise_sort = sorted(combined_arr, key =  lambda x: x[1])

#unzip the sorted arrays
sorted_arr1, sorted_arr2 = zip(*arr1_wise_sort)

print(sorted_arr1, sorted_arr2)

sorted_arr1, sorted_arr2 = zip(*arr2_wise_sort)

print(sorted_arr1, sorted_arr2)

