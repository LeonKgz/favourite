


def swapNodes(indexes, queries):
    # Write your code here
    
    ret = []
    for q in queries:
        curr_d = q
        k = 1
        max_depth = get_depth(indexes, 1, 0)
        
        while curr_d <= max_depth:
            curr_d *= k
            k += 1
            swap_at_depth(indexes, 1, 1, curr_d)
            
        ret.append(traversal(indexes, 1))    
        
    return ret


def swap_at_depth(indexes, j, curr_depth, target_depth):
    if (j == -1):
        return
    
    root = j - 1
    left = indexes[root][0]
    right = indexes[root][1]
    
    if (curr_depth == target_depth):
        indexes[root][0] = right
        indexes[root][1] = left
    
    if (curr_depth > target_depth):
        return
        
    swap_at_depth(indexes, left, curr_depth + 1, target_depth)
    swap_at_depth(indexes, right, curr_depth + 1, target_depth)
        
def get_depth(indexes, j, curr_depth):
    
    if (j == -1):
        return curr_depth
    
    root = j - 1
    left = indexes[root][0]
    right = indexes[root][1]
    
    maxval = curr_depth
    
    l_depth = get_depth(indexes, left, curr_depth + 1)
    if (l_depth > maxval):
        maxval = l_depth
        
    r_depth = get_depth(indexes, right, curr_depth + 1)
    if r_depth > maxval:
        maxval = r_depth
        
    return maxval
    
def traversal(indexes, j):
    ret = []
    
    root = j - 1
    left = indexes[root][0]
    right = indexes[root][1]
    
    if left != -1:
        ret += traversal(indexes, left)
    ret += [root + 1]
    if right != -1:
        ret += traversal(indexes, right)
    
    return ret
    
