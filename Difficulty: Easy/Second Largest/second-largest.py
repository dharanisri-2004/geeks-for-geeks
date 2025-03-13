#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        largest = -1
        second_largest = -1
        for i in range(n):
            if arr[i] > largest:
                largest = arr[i]
        for i in range(n):
            if arr[i] > second_largest and arr[i] != largest:
                second_largest = arr[i]
        return second_largest



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends