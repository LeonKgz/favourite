def activityNotifications(expenditure, d):
    # Write your code here
    
    # deque is always sorted and stores the last d elements from expenditure
    res = 0
    cnt = 0
    
    encountered = []
    
    counts = []
    
    for i in range(201):
      counts.append(0)

    for e in expenditure:
        
        if (cnt >= d):
          median = getMedian(counts, d)
          if (e >= median * 2):
              res += 1
          first = encountered[-d]
          counts[first] -= 1
        counts[e] += 1

        cnt += 1    
        encountered.append(e)

    return res

def getMedian(arr, d):
  
  if (d % 2 == 0):
    
    m1 = None
    m2 = None

    count = 0
    for i in range(len(arr)):
      count += arr[i]
      if (m1 == None and count >= d/2):
        m1 = i
      if (m2 == None and count >= d/2 + 1):
        m2 = i
        break

    return (m1 + m2) / 2.0

  else:
    count = 0
    for i in range(len(arr)):
      count += arr[i]
      if (count >= d/2):
        return i

#print(activityNotifications([1 ,2 ,3 ,4 ,4], 4))
#exit(0)


def read_input(name):
  with open(name, 'r') as f:
    content = [int(i) for i in f.readlines()[1].split(" ")]
    print(activityNotifications(content, 10000))

read_input("input10.txt")
