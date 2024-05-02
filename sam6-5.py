def is_subsequence(main_list, subsequence):
    it = iter(main_list)
    return all(item in it for item in subsequence)

test1 = is_subsequence([2, 2, 5, 4, 5], [2, 2, 5])
test2 = is_subsequence([1, 2, 3, 4, 5], [1, 2])
test3 = is_subsequence([5, 6, 7, 8, 9], [5, 8, 7])

print(f"Test 1: {test1}")
print(f"Test 2: {test2}")
print(f"Test 3: {test3}")
