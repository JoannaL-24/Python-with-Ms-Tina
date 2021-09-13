import time

def binarySearch(list, finding, down, up):
    mid = int((up-down)/2)
    
    if (up-down <= 0):
        return -1
    if (list[mid] == finding):
        return mid
    elif (list[mid] > finding):
        return binarySearch(list, finding, 0, mid)
    else:
        return binarySearch(list, finding, mid+1, len(list))

startTime = time.time()
list = [1,2,3,4,5,6]
print(binarySearch(list,3, 0, len(list)))
print("Time: ", (time.time() - startTime)*1000)

