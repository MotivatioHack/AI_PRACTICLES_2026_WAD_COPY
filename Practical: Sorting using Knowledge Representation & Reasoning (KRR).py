# Practical: Sorting using Knowledge Representation & Reasoning (KRR)

# -----------------------------
# Bubble Sort Function
# Rule:
# IF current element > next element
# THEN Swap
# -----------------------------

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            # Reasoning Rule
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# -----------------------------
# Selection Sort Function
# Rule:
# Find minimum element
# Place it in correct position
# -----------------------------

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i+1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# -----------------------------
# Main Program
# -----------------------------

numbers = [64, 25, 12, 22, 11]

print("Original List:")
print(numbers)


# Bubble Sort
bubble_result = bubble_sort(numbers.copy())

print("\nBubble Sort Result:")
print(bubble_result)


# Selection Sort
selection_result = selection_sort(numbers.copy())

print("\nSelection Sort Result:")
print(selection_result)


# Complexity Analysis
print("\nComplexity Analysis:")

print("Bubble Sort:")
print("Time Complexity = O(n^2)")
print("Space Complexity = O(1)")

print("\nSelection Sort:")
print("Time Complexity = O(n^2)")
print("Space Complexity = O(1)")
