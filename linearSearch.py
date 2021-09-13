import time

def linearSearch(list, finding):
    index = []
    for i in range(len(list)):
        if list[i] == finding:
            index.append(i)
    if (len(index) == 0):
        print("Not in the list")
        return -1
    return index

startTime = time.time()
list = [1,2,3,4,5,5,6,7]
finding = 5
index = linearSearch(list, finding)
if (len(index) != 0):
    print(index)

print("Time: ", (time.time() - startTime)*1000)