def countInversions(arr):
    # Write your code here
    cnt = 0
    arr, cnt = merge_sort(arr, 0, len(arr), cnt)
    return cnt

def merge_sort(arr, left, right, counter):

    if (right - left == 1):
      return counter

    half = int((right - left) / 2) + left
    
    left_right = half
    right_left = half
    #print(left)
    #print(left_right)
    #print(right_left)
    #print(right)
    #exit(0)

    counter = merge_sort(arr, left, left_right, counter)
    counter = merge_sort(arr, right_left, right, counter)
    counter = merge(arr, left, left_right, right_left, right, counter)
    
    return counter

def merge(arr, a1, a2, b1, b2, counter):
    
    ret = []
    
    c1 = 0
    c2 = 0

    counter = counter
    l1 = a2 - a1
    l2 = b2 - b1

    while (c1 < l1 and c2 < l2):
 
        
        if (arr[a1:a2][c1] <= arr[b1:b2][c2]):
            ret.append(arr[a1:a2][c1])
            c1 += 1
        else:
            counter += len(arr[a1:a2][c1:])
            ret.append(arr[b1:b2][c2])
            c2 += 1

    if (l1 == c1):
      ret += arr[b1:b2][c2:]

    if (l2 == c2):
      ret += arr[a1:a2][c1:]
            
    return counter

arr = [7, 5, 3, 1]
left = 0
right = len(arr)
print(merge_sort(arr, left, right, 0))
