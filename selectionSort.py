def selectionSort(list):
    for i in range(len(list)-1):
        smallest = i
        for j in range(i, len(list)):
            if (list[smallest] > list[j]):
                smallest = j
        temp = list[i]
        list[i] = list[smallest]
        list[smallest] = temp
    return list

nums = [5,1,1,2,0,0]
print(selectionSort(nums))

arr = input("Enter array: ").split()
print(arr)
print("sorted: ", selectionSort(arr))