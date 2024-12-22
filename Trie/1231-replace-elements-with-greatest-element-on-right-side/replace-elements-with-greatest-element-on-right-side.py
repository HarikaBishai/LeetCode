class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxSoFar = -1

        for i in range(n-1, -1, -1):
            curr = arr[i]

            arr[i] = maxSoFar
            maxSoFar = max(curr, maxSoFar)
        return arr

