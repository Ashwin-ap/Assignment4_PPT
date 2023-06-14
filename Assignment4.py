Question 1
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

def find_common_elements(arr1, arr2, arr3):
    p1 = p2 = p3 = 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr2[p2] < arr3[p3]:
            p2 += 1
        else:
            p3 += 1

    return result

Question 2
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

def find_disjoint_integers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result1 = [num for num in nums1 if num not in set2]
    result2 = [num for num in nums2 if num not in set1]
    return [result1, result2]

Question 3
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


Question 4
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

def array_pair_sum(nums):
    nums.sort()
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    return max_sum


Question 5
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

def arrange_coins(n):
    left = 0
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        series_sum = (mid * (mid + 1)) // 2

        if series_sum <= n:
            left = mid + 1
        else:
            right = mid - 1

    return right


Question 6
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1

    return result

Question 7
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

def max_count(m, n, ops):
    min_ai = m
    min_bi = n

    for ai, bi in ops:
        min_ai = min(min_ai, ai)
        min_bi = min(min_bi, bi)

    return min_ai * min_bi


Question 8
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def rearrange_array(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result

