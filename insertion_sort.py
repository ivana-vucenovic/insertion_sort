def insertionSort(nlist):
   for index in range(1,len(nlist)):

    currentvalue = nlist[index]
    position = index

    while position>0 and nlist[position-1]>currentvalue:
        nlist[position]=nlist[position-1]
        position = position-1

    nlist[position]=currentvalue

nlist = [9,1,8,2,7,3,6,4,5]
insertionSort(nlist)
print(nlist)