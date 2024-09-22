def nimabani (n,b):
  if n not in b:
    return -1


  l=len (n)
  for i in range(len (b)) :
    if n==b[i:(i+l)]:
      return i


