

def binarysearh(arr, target):
    left = 0
    right = len(arr)-1

    while(left <= right):
        #get the middle of the array, diving the length of array
        mid = (left+right)//2
        
        if (arr[mid] == target):
            return mid
        # check if target is greater than item in the middle index , if yes move the left index to middle + 1
        elif (arr[mid] < target):
            left = mid+1
        else:
            right = mid-1

    return -1

arr = [1,2,3,4,5,6,8,9,10,11]
target = 11

result = binarysearh(arr, target)

if result != -1:
    print("Element is at %d index", result)
else:
    print ("there is no such element")