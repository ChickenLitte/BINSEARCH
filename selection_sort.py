#for i o to n
#fidn the ith smallest
#swap it into pos 

def selection_sort(collection):
    smallestElement = 0
    for i in range(0,len(collection)):
        smallestElement = i
        for j in range(i,len(collection)):
            if collection[j]<=collection[smallestElement]:
                smallestElement = j
        collection[i],collection[smallestElement] = collection[smallestElement],collection[i]
    return collection

array = [6, 5, 3, 7, 2, 8, 4]
print(selection_sort(array))
