import timeit
import random

def insertion_sort(lst):
    lst = lst.copy()
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Якщо в лівій або правій половині залишилися елементи, 
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

# Тестові дані
small_data = [5, 3, 8, 4, 2]
medium_data = [random.randint(1, 100) for _ in range(100)]
large_data = [random.randint(1, 1000) for _ in range(1000)]

# Порівняння швидкості
print("📊 ПОРІВНЯННЯ ШВИДКОСТІ")
print("=" * 50)

print(f"\n🔸 Малий масив ({len(small_data)} елементів):")
time1 = timeit.timeit(lambda: insertion_sort(small_data), number=10000)
time2 = timeit.timeit(lambda: merge_sort(small_data), number=10000)
time3 = timeit.timeit(lambda: sorted(small_data), number=10000)
print(f"insertion_sort: {time1:.4f} сек")
print(f"merge_sort:     {time2:.4f} сек")
print(f"sorted():       {time3:.4f} сек")

print(f"\n🔸 Середній масив ({len(medium_data)} елементів):")
time1 = timeit.timeit(lambda: insertion_sort(medium_data), number=1000)
time2 = timeit.timeit(lambda: merge_sort(medium_data), number=1000)
time3 = timeit.timeit(lambda: sorted(medium_data), number=1000)
print(f"insertion_sort: {time1:.4f} сек")
print(f"merge_sort:     {time2:.4f} сек")
print(f"sorted():       {time3:.4f} сек")

print(f"\n🔸 Великий масив ({len(large_data)} елементів):")
time1 = timeit.timeit(lambda: insertion_sort(large_data), number=100)
time2 = timeit.timeit(lambda: merge_sort(large_data), number=100)
time3 = timeit.timeit(lambda: sorted(large_data), number=100)
print(f"insertion_sort: {time1:.4f} сек")
print(f"merge_sort:     {time2:.4f} сек")
print(f"sorted():       {time3:.4f} сек")

# Рейтинг швидкості
print(f"\n🏆 РЕЙТИНГ ЗА ШВИДКІСТЮ (для великих масивів):")
results = [
    ("sorted()", time3),
    ("merge_sort", time2), 
    ("insertion_sort", time1)
]
results.sort(key=lambda x: x[1])
for i, (name, time) in enumerate(results, 1):
    print(f"{i}. {name}: {time:.4f} сек")