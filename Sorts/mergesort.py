def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
print("Array: ", arr)
mergeSort(arr)
n = len(arr)
print("Sorted array: ", arr)

# Сортування починається з розбиття набору даних на окремі частини та сортування частин.
# Потім він об'єднує частини так, щоб гарантувати, що вона відсортувала об'єднану частину.
# Сортування та об'єднання продовжуються до тих пір, поки весь набір даних знову не стане єдиним цілим.

# Основні переваги сортування злиттям:
# Є стабільним - порядок елементів з однаковим значенням зберігається після сортування.

# Основні недоліки сортування злиттям:
# Може вимагати більше пам'яті для зберігання елементів під час виконання.
# Є менш ефективним для великих масивів даних.

# Гірший, середній, найкращий час - O(n log(n))
# Просторова складність - O(n)
# Допоміжний простір - O(n)