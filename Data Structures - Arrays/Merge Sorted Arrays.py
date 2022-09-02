

#array1 = [3,4,1]
#array2 = [8,2,5]

#def mergeSortedArrays(array1, array2):
#    array3 = array1 + array2
#    array3.sort()
#    return array3

#result = mergeSortedArrays(array1, array2)

#In interviews we must solve like this

def mergeSortedArray(array1,array2):
  if len(array1) == 0 or len(array2) == 0:
    return array1+array2

  mergedArray=[]
  indexArray1=0
  indexArray2=0

  while indexArray1<len(array1) and indexArray2<len(array2):

    if array1[indexArray1] <= array2[indexArray2]:
      mergedArray.append(array1[indexArray1])
      indexArray1+=1

    elif array2[indexArray2] < array1[indexArray1]:
      mergedArray.append(array2[indexArray2])
      indexArray2+=1

  return mergedArray

list1 = [1,3,4,6,20]
list2 = [2,3,4,5,6,9,11,76]
array = mergeSortedArray(list1,list2)
print(array)




