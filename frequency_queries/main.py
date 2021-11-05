def freqQuery(queries):
    # storage keeps track of current 
    storage = {}
    # keeps each number of occurences of a number in storage  
    counters = {}
    
    for q in queries:
        
        operation = q[0]
        val = q[1]
        
        if (operation == 1):
            
            # previous counter
            prev = storage.get(val, 0)
            # current counter
            curr = prev + 1 
            
            storage[val] = curr
            
            if (curr not in counters):
                counters[curr] = set()
                counters[curr].add(val)
                
            if (prev != 0 and val in counters[prev]):
                counters[prev].remove(val)
            
        if (operation == 2):
            
            # previous counter
            prev = storage.get(val, 0)
            # current counter
            curr = prev - 1 
            storage[val] = curr if curr > 0 else 0 
            
            if (curr in counters and val in counters[curr]):
                counters[curr].remove(val)
                
            if (prev != 0 and val in counter[prev]):
                counters[prev].remove(val)
         
        if (operation == 3):
            if (val in counters and len(counters[val]) > 0):
                print(1)
