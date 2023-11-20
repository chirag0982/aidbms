def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mini= i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

def findMin(V):
    # All denominations of Indian Currency
    deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = len(deno)
    # Initialize Result
    ans = []
    # Traverse through all denominations
    i = n - 1
    while(i >= 0):
        # Find denominations
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])
        i -= 1
    # Sort result using selection sort
    selectionSort(ans)
    # Print result
    for i in range(len(ans)):
        print(ans[i], end=" ")

# Driver Code
if __name__ == '__main__':
    n = int(input("Enter the amount: "))
    print("Following is the minimal number of change for", n, ": ", end="")
    findMin(n)
