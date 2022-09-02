

#array1 = [3,4,1]
#array2 = [8,2,5]

#def mergeSortedArrays(array1, array2):
#    array3 = array1 + array2
#    array3.sort()
#    return array3

#result = mergeSortedArrays(array1, array2)

#In interviews we must solve like this

def mergeSortedArray(a,b):
  if len(a) == 0 or len(b) == 0:
    return a+b
  
  mylist=[]
  i=0
  j=0

  while i<len(a) and j<len(b):

    if a[i] <= b[j]:
      mylist.append(a[i])
      i+=1

    elif b[j] < a[i]:
      mylist.append(b[j])
      j+=1

  return mylist + a[i:] + b[j:]

a = [1,3,4,6,20]
b = [2,3,4,5,6,9,11,76]
array = mergeSortedArray(a,b)
print(array)


