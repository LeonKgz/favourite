first = ["9", "2"]
second = ["9", "2", "1"]
ret = []

if (len(second) > len(first)):
  temp = first
  first = second
  second = temp

queue = []

f = len(first) - 1
s = len(second) - 1

while(not (f == -1 and s == -1)):
  
  curr = 0
  left = 0
  right = 0

  if (len(queue) > 0):
    curr = queue.pop()
  
  if f != -1:
    left = int(first[f])
  
  if s != -1:
    right = int(second[s])

  res = left + right + curr
  
  if (res >= 10):
    queue.append(1)

  res = res % 10
  ret = [str(res)] + ret

  if (f > -1):
    f -= 1

  if (s > -1):
    s -= 1

print(queue)
if (len(queue) > 0):
  curr = queue.pop()
  ret = [str(curr)] + ret

print(ret)
