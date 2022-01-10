a = [1, 4, 5]
c = [1, 2, 3]
b = [2, 3, 3]

# bb >= aa
def get_d(aa, bb):
  
  d = {}

  a_cnt = 0
  b_cnt = 0

  while a_cnt < len(aa):
    acurr = aa[a_cnt]
    bcurr = bb[b_cnt]
#    print(f"{acurr}, {bcurr}")

    if (acurr <= bcurr):
      d[bcurr] = d.get(bcurr, 0) + 1
      a_cnt += 1
    else:
      # next b elemnet has at least the same range...

      if (b_cnt + 1 == len(bb)):
        return d

      if bcurr not in d:
        d[bcurr] = 0

      d[bb[b_cnt + 1]] = d.get(bcurr, 0)

      b_cnt += 1

  if b_cnt < len(bb):
    for i in range(b_cnt, len(bb)):
      d[bb[i]] = len(aa)


  return d

#print(get_d(a, b))
#print(get_d(c, b))

def final(a, b, c):
  
  # Removing duplicates!
  a = list(dict.fromkeys(a))   
  b = list(dict.fromkeys(b))   
  c = list(dict.fromkeys(c))   

  # All arrays must be sorted!
  a = sorted(a)
  b = sorted(b)
  c = sorted(c)

  ba = get_d(a, b)
  bc = get_d(c, b)

  d = {}
  
  for i in b:
    d[i] = d.get(i, 0) + 1
  
  ret = 0

  for i in d.keys():
    ret += ba[i] * bc[i]

  return ret

print(final(a, b, c))



