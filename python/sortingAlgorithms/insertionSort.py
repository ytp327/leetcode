def insertionSort(A):
    for i in range(0, len(A)):
        for j in range(0, i):
            if A[i]< A[j]:
                A[i], A[j] = A[j], A[i]
                continue
A=[5,4,3,2,1]
insertionSort(A)
print(A)