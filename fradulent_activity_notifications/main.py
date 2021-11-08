def insert_sort(deque, element):
    curr = len(deque)
    
    if (curr == 0):
        deque.append(element)
        return 0
    
    if (curr == 1):
        if (element > deque[0]):
            deque.append(element)
            return 1
        else:
            deque.insert(0, element)
            return 0
    
    curr = len(deque)
        
    while (element < deque[curr-1]):
        curr -= 1
        if (curr == -1):
            deque.insert(0, element)
    
    deque.insert(curr, element)
    return curr    
            
def activityNotifications(expenditure, d):
    # Write your code here
    
    # deque is always sorted and stores the last d elements from expenditure
    deque = []
    res = 0
    cnt = 0
    
    encountered = []
    history = {}
    
    for e in expenditure:
        cnt += 1
        if (cnt % 1000 == 0):
          print(cnt)
        encountered.append(e)
        # print(f"{e} is incoming")
        # print("-------")
        if (len(deque) == d):
            # now need to sort deque and calculate median
            
            # if insert sort into deque, then we need to know what element was added d times before and 
            # remove it (don't care about repeated values)
            
            idx = int(d / 2) if d % 2 == 1 else int(d/2) + 1
            
            if (d % 2 == 0):
                median = (deque[int(d / 2)] + deque[int(d / 2) - 1]) / 2
            else:
                median = deque[int(d / 2)]
                
            if (e >= median * 2):
                res += 1
            
            deque.remove(encountered[-d - 1])
            # print(history)
            # print(encountered[-d])
            # print(history[encountered[-d]])
            # print(f"now deleting {encountered[-d-1]}")
            # del deque[history[encountered[-d-1]]]
            idx = insert_sort(deque, e)
            history[e] = idx
            
        else:
            idx = insert_sort(deque, e)
            history[e] = idx
            continue
    return res


def read_input(name):
  with open(name, 'r') as f:
    content = [int(i) for i in f.readlines()[1].split(" ")]
    print(activityNotifications(content, 10000))

read_input("input10.txt")
