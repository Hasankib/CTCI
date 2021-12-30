def generatePermuatations(A:[int]) -> [[int]]:
    def generateSubPerm(i):
        if i == len(A) - 1:
            results.append(A.copy())
            return

        for j in range(i,len(A)):
            A[i], A[j] = A[j], A[i]
            print("i is",i,"A switched to", A)
            generateSubPerm(i + 1)
            A[i],A[j] = A[j], A[i]

    results = []
    generateSubPerm(0)
    return results

print(generatePermuatations([2,3,5,7]))