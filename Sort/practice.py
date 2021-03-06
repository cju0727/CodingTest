array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬 O(N^2)
# for i in range(len(array)):
#     min_index = i
#     for j in range(i, len(array)):
#         if array[j] < array[min_index]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
    
# print(array)


# 삽입 정렬 O(N^2)이지만 거의 정렬되있는 경우 퀵 정렯보다 더 효율적이다.
# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break

# print(array)

# 퀵 정렬 O(NlogN), 최악의 경우에도 O(N^2)을 보장한다.
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end

#     while left <= right: # 인덱스가 엇갈리지 않았을 때
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1

#         if left > right: # 인덱스가 엇갈렸을 때
#             array[right], array[pivot] = array[pivot], array[right]
#         else: # 그 외는 left와 right 자리를 바꿔줌
#             array[left], array[right] = array[right], array[left]
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)

# quick_sort(array, 0, len(array) - 1)
# print(array)

# 계수 정렬
# array2 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# count = [0] * (max(array) + 1)

# for a in array2:
#     count[a] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end = ' ')

# 파이썬 sorted
# result = sorted(array)
# print(result)

# or
# array.sort()
# print(array)

array3 = [('banana', 2), ('apple', 5), ('당근', 3)]

result = sorted(array3, key = lambda x : x[1])
print(result)

