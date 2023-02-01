# 오름차순 삽입정렬
def insertion_sort(array) :
    for i in range(1, lena(array)) :
        for j in range(i, 0, -1) :
            if array[j] < array[j-1] :
                array[j], array[j-1] = array[j-1], array[j]
            else :
                break
    return array 

# 내림차순 삽입정렬
def insertion_sort_reverse(array) :
    for i in range(1, lena(array)) :
        for j in range(i, 0, -1) :
            if array[j] < array[j-1] :
                array[j], array[j-1] = array[j-1], array[j]
            else :
                break
    array.reverse()
    return array 

'''
array =  [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #오름차순
result = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] #내림차순
'''