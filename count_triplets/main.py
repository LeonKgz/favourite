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
print(countTriplets([1, 5, 5, 25, 125], 5))
