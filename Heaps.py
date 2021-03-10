def heapify(arr , n , i):
    
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    while left < n and arr[left] > arr[largest]:
        largest = left
    while right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr , n , largest)
       

def insert(arr , new):
    size = len(arr)
    arr.append(new)
    if size != 0:
        for i in range((len(arr) // 2) - 1 , -1 , -1):
            heapify(arr , len(arr) , i)

def delete(arr , tar):
    size = len(arr)
    for i in range(size):
        if arr[i] == tar:
            break

    arr[i] , arr[size - 1] = arr[size - 1] , arr[i]

    arr.pop()
    for j in range((size // 2) - 1 , -1 , -1):
        heapify(arr , len(arr) , j)        
    
def heapsort(arr):

    final = []

    # Heapify
    for i in range((len(arr) // 2) , -1 , -1):
        heapify(arr , len(arr) , i)
    
    # Delete from the top and heapify simultaniously

    for i in range(len(arr) - 1, -1 , -1):
        arr[0] , arr[i] = arr[i] , arr[0]
        final.append(arr.pop())

        heapify(arr , i , 0)

    print(final)


arr = []
# insert(arr , 3)
# insert(arr , 4)
# insert(arr , 9)
# insert(arr , 5)
# insert(arr , 2)
# print(arr)
# delete(arr , 4)
# print(arr)

insert(arr , 1)
insert(arr , 12)
insert(arr , 9)
insert(arr , 5)
insert(arr , 6)
insert(arr , 10)
print(arr)
delete(arr , 6)
print(arr)
heapsort(arr)

