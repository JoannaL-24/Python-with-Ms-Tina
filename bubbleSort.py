def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(i,len(list)):
            if (list[i] > list[j]):
                temp=list[j]
                list[j]=list[i]
                list[i]=temp
    return list

nums = [2,0,2,1,1,0] 
print(bubble_sort(nums))

arr = input("Enter array: ").split()
print(arr)
print("sorted: ", bubble_sort(arr))