#placing the 1st largest element at the end of the list
#placing the 2nd largest element at the 2nd last position of the list
#so on and so forth
def bubble(collection):
    previous = None
    for j in range(len(collection)):
        for i in range(len(collection)-1-j):
            previous = collection[i]
            if collection[i+1]<previous:
                collection[i]=collection[i+1]
                collection[i+1]=previous
    return collection

array=[5,3,8,6,2000,7,2]
print(bubble(array))

