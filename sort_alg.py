# Сравнение алгоритмов сортировки 

def gen(n, m):
    """
    генератор списка
    :param n: число элементов списка
    :param m: max значение в списке
    :return: list
    """
    import random as rnd
    A = []
    for _ in range(n):
        A.append(rnd.randint(0, m))
    return A

def bubble_sort(A):
    """
    сортировка пузырьком (bubble sort)
    сравниваем 2 соседних элемента
    если левый больше правого, то переставляем местами
    сложность O(n^2)
    :param A:
    :return:
    """
    swapped = True  # флажок, что произошла перестановка
    while swapped:  # если перестановок не было, то далее не считаем
        swapped = False
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i] # меняем местами
                swapped = True
    return A

def selection_sort(A):
    """
    сортировка выборкой
    сначала из всех элементов находится наименьший, ставится на 1 место
    далее повторяем для оставшихся элементов
    сложность O(n^2), но с меньшим коэффициентом
    :param A:
    :return:
    """
    for i in range(len(A)):
        # i - номер стартового элемента
        lowest_elem_index = i # считаем начальный элемент минимальным
        for j in range(i+1, len(A)):
            if A[j] < A[lowest_elem_index]:
                lowest_elem_index = j
        A[i], A[lowest_elem_index] = A[lowest_elem_index], A[i]
    return A

def merge(left_list, right_list):
    """
    сортировка слиянием
    сложность O(n*logn)
    :param left_list: сортированный список 1
    :param right_list: сортированный список 2
    :return:
    """
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):  
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)

if __name__ == "__main__":
    import time
    import copy
    tests = [0, 1, 2, 3, 4, 5, 6, 7]
    test = 0

    while test in tests:    
        print('Введите номер теста (от 0 до 7):')
        print('тест #0 - время сортировки пузырьком и выборкой (сравнение при разных n)')
        print('тест #1 - время сортировки слиянием и Timsort (сравнение при разных n)')
        print('тест #2 - сортировка случайного списка тремя способами, замер времени')
        print('тест #3 - время сортировки 4 случайных списков разного размера тремя способами')
        print('тест #4 - время сортировки пузырьком для 10 случайных списков разного размера')
        print('тест #5 - время сортировки выборкой для 10 случайных списков разного размера')
        print('тест #6 - время сортировки слиянием для 10 случайных списков разного размера')
        print('тест #7 - время сортировки Python для 10 случайных списков разного размера')
        test = int(input())    # номер теста

        if test == 0:
            nums = [2000, 4000, 6000, 8000]
            time_bubble = []
            time_selection = []

            for n in nums:
                A = gen(n, 100)
                B = copy.copy(A)
                C = copy.copy(A)
                t1 = time.time()
                B = bubble_sort(B)
                t = round(time.time() - t1, 3)
                time_bubble.append(t)
                t1 = time.time()
                C = selection_sort(C)
                t = round(time.time() - t1, 3)
                time_selection.append(t)
            print('-- Сортировка пузырьком и выборкой (сравнение) --')
            print('Число элементов списка:')
            print(*nums, sep='\t')
            print('Сортировка пузырьком. Время:')
            print(*time_bubble, sep='\t')
            print('Сортировка выборкой. Время:')
            print(*time_selection, sep='\t')
            print()

        if test == 1:
            nums = [200000, 400000, 600000, 800000]
            time_merge = []
            time_timsort = []

            for n in nums:
                A = gen(n, 100)
                B = copy.copy(A)
                C = copy.copy(A)
                t1 = time.time()
                B = merge_sort(B)
                t = round(time.time() - t1, 3)
                time_merge.append(t)
                t1 = time.time()
                C.sort()
                t = round(time.time() - t1, 3)
                time_timsort.append(t)
            print('-- Сортировка слиянием и timsort (сравнение) --')
            print('Число элементов списка:')
            print(*nums, sep='\t')
            print('Сортировка слиянием. Время:')
            print(*time_merge, sep='\t')
            print('Сортировка timsort. Время:')
            print(*time_timsort, sep='\t')
            print()

        if test == 2:
            print('Введите размер списка (число от 10 до 10000:')
            n = int(input())
            A = gen(n, 100)
            B = copy.copy(A)
            print('A =', A)
            t1 = time.time()
            B = bubble_sort(B)
            t = round(time.time() - t1, 3)
            print('B =', B)
            print('Сортировка пузырьком. Время =', t)

            C = copy.copy(A)
            t1 = time.time()
            C = selection_sort(C)
            t = round(time.time() - t1, 3)
            print('C =', C)
            print('Сортировка выборкой. Время =', t)

            D = copy.copy(A)
            t1 = time.time()
            D = merge_sort(D)
            t = round(time.time() - t1, 3)
            print('D =', D)
            print('Сортировка слиянием. Время =', t)
            print()

        if test == 3:
            times_bubble_sort = []
            times_selection_sort = []
            times_merge_sort = []
            nums = [1000, 2000, 4000, 8000]
            for n in nums:
                for _ in range(5):
                    A = gen(n, 100)
                    B = copy.copy(A)
                    t1 = time.time()
                    B = bubble_sort(B)
                    t = round(time.time() - t1, 5)
                    times_bubble_sort.append(t)

                    S = copy.copy(A)
                    t1 = time.time()
                    S = selection_sort(S)
                    t = round(time.time() - t1, 5)
                    times_selection_sort.append(t)

                    M = copy.copy(A)
                    t1 = time.time()
                    M = merge_sort(M)
                    t = round(time.time() - t1, 5)
                    times_merge_sort.append(t)

            times_bubble = [round(sum(times_bubble_sort[:5])/5, 5),
                            round(sum(times_bubble_sort[5:10])/5, 5),
                            round(sum(times_bubble_sort[10:15])/5, 5),
                            round(sum(times_bubble_sort[15:])/5, 5)]
            times_selection = [round(sum(times_selection_sort[:5])/5, 5),
                               round(sum(times_selection_sort[5:10])/5, 5),
                               round(sum(times_selection_sort[10:15])/5, 5),
                               round(sum(times_selection_sort[15:])/5, 5)]
            times_merge = [round(sum(times_merge_sort[:5])/5, 5),
                           round(sum(times_merge_sort[5:10])/5, 5),
                           round(sum(times_merge_sort[10:15])/5, 5),
                           round(sum(times_merge_sort[15:])/5, 5)]
            print('-- Тест времени работы алгоритмов сортировки --')
            print('Число элементов списка:')
            print(*nums, sep='\t')
            print('Сортировка пузырьком. Время:')
            print(*times_bubble, sep='\t')
            print('Сортировка выборкой. Время:')
            print(*times_selection, sep='\t')
            print('Сортировка слиянием. Время:')
            print(*times_merge, sep='\t')
            print()

        if test == 4:
            times_bubble_sort = []
            nums = []
            for i in range(1, 11):
                nums .append(1000 * i)

            for n in nums:
                A = gen(n, 100)
                M = copy.copy(A)
                t1 = time.time()
                M = bubble_sort(M)
                t = round(time.time() - t1, 5)
                times_bubble_sort.append(t)
            print('-- Сортировка пузырьком --')
            print('Число элементов списка:')
            print(*nums, sep='\t')
            print('Время сортировки:')
            print(*times_bubble_sort, sep='\t')
            print()

        if test == 5:
            times_selection_sort = []
            nums = []
            for i in range(1, 11):
                nums .append(2000 * i)

            for n in nums:
                A = gen(n, 100)
                M = copy.copy(A)
                t1 = time.time()
                M = selection_sort(M)
                t = round(time.time() - t1, 5)
                times_selection_sort.append(t)
            print('-- Сортировка выборкой --')
            print('Число элементов списка:')
            print(*nums, sep='\t')
            print('Время сортировки:')
            print(*times_selection_sort, sep='\t')
            print()

        if test == 6:
            times_merge_sort = []
            nums = []
            for i in range(1, 11):
                nums .append(100000 * i)

            for n in nums:
                A = gen(n, 100)
                M = copy.copy(A)
                t1 = time.time()
                M = merge_sort(M)
                t = round(time.time() - t1, 5)
                times_merge_sort.append(t)
            print('-- Сортировка слиянием --')
            print('Число элементов списка:')
            print(*nums, sep='\t')
            print('Время сортировки:')
            print(*times_merge_sort, sep='\t')
            print()

        if test == 7:
            times_sort = []
            nums = []
            for i in range(1, 11):
                nums .append(200000 * i)

            for n in nums:
                A = gen(n, 100)
                M = copy.copy(A)
                t1 = time.time()
                M.sort()
                t = round(time.time() - t1, 5)
                times_sort.append(t)
            print('-- Сортировка Python --')
            print('Число элементов списка:')
            print(*nums, sep='\t')
            print('Время сортировки:')
            print(*times_sort, sep='\t')
            print()
    


