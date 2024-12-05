#for i o to n
#fidn the ith smallest
#swap it into pos 

#but recursive

def selection_sort(collection,done=[],smallestElement=0):
    
    if len(collection) == 0:return done#base case
    
    for j in range(len(collection)):
        if collection[j]<=collection[smallestElement]:smallestElement = j#sets the new smallest element
    
    collection[0],collection[smallestElement] = collection[0],collection[smallestElement]#swap stuff
    
    done.append(collection.pop(smallestElement))#append to the done pile and remove from the collection
    
    return selection_sort(collection,done)

array = [6, 5, 3, 7, 2, 8, 4]
print(selection_sort(array))
