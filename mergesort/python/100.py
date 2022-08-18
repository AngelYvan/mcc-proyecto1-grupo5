def mergesort(a):
  if len(a) == 1:
    return a
  elif len(a) == 2:
    if a[0] > a[1]:
      return [a[1], a[0]]
    else:
      return a

  p = len(a)//2
  m1 = mergesort(a[:p])
  m2 = mergesort(a[p:])

  ret = []
  while 1:
    if len(m1) > 0 and len(m2) > 0:
      if m1[0] <= m2[0]:
        ret.append(m1[0])
        m1 = m1[1:]
      else:
        ret.append(m2[0])
        m2 = m2[1:]
    elif len(m1) > 0:
      ret += m1
      m1 = []
    elif len(m2) > 0:
      ret += m2
      m2 = []
    else:
      break
  return ret

a = [ 21,2,61,63,50,35,46,42,3,80,14,80,7,65,27,32,23,7,4,72,96,37,10,87,60,61,46,38,85,77,99,38,54,93,35,28,19,52,100,62,67,71,85,78,57,27,45,20,61,22,11,70,100,79,74,27,64,82,7,56,15,73,68,13,30,39,34,94,17,70,32,37,49,34,51,56,3,91,77,62,56,65,98,92,61,75,11,91,35,54,63,16,24,22,11,28,43,15,4,53]
print(mergesort(a))


