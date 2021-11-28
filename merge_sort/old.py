def countInversions(arr):
    # Write your code here
    cnt = 0
    arr, cnt = merge_sort(arr, cnt)
    return cnt

def merge_sort(arr, counter):

    if (len(arr) == 1):
      return arr, counter

    half = int(len(arr) / 2)
    left_half = arr[:half]
    right_half = arr[half:]

    left_half, counter = merge_sort(left_half, counter)
    right_half, counter = merge_sort(right_half, counter)
    ret, cnt = merge(left_half, right_half, counter)
    return ret, cnt 

def merge(arr1, arr2, counter):
    
    ret = []
    a1 = 0
    a2 = 0
    counter = counter
    l1 = len(arr1)
    l2 = len(arr2)

    while (a1 < l1 and a2 < l2):
 
        if (arr1[a1] <= arr2[a2]):
            ret.append(arr1[a1])
            a1 += 1
        else:
            counter += len(arr1[a1:])
            ret.append(arr2[a2])
            a2 += 1

    if (l1 == a1):
      ret += arr2[a2:]

    if (l2 == a2):
      ret += arr1[a1:]
            
    return ret, counter

