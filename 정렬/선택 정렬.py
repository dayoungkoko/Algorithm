# 오름차순 선택정렬
def selection_sort(array) :
    for i in range(len(array)) :
        min_index = i
        for j in range(i+1, len(array)) :
            if array[j] < array[min_index] :
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# 내림차순 선택정렬
def selection_sort_reverse(array) :
    for i in range(len(array)) :
        min_index = i
        for j in range(i+1, len(array)) :
            if array[j] < array[min_index] :
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    array.reverse()
    return array

'''
ex.
array =  [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #오름차순
result = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] #내림차순
'''