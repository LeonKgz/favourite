def countTriplets(arr, r):

  seconds = {}
  thirds = {}
  counts = {}
  for a in arr:
    if (a in counts):
      counts[a] += 1
    else:
      counts[a] = 1
    ar = a * r
    arr = a * r * r
    if (ar not in seconds):
      seconds[ar] = 0
    if (arr not in thirds):
      thirds[arr] = 0
    if (a in seconds):
      seconds[a] += 1
      
    if (a in thirds):
      thirds[a] += 1

  ret = 0

  if (r == 1):
  
    for val, cnt in counts.items():
      n = cnt
      top = n * (n-1) * (n-2)
      bottom = 6
      ret += int(top / 6)
    return ret
  #print(counts)
  #print(seconds)
  #print(thirds)
  for val, counter in thirds.items():
    if (counter != 0):
      ar = int(val / r)
      a = int(ar / r)

      ret += (counter * seconds[ar] * counts[a])
  return ret

print(countTriplets([1, 4, 16, 64], 4))
print(countTriplets([1, 3, 9, 9, 27, 81], 3))
print(countTriplets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))

