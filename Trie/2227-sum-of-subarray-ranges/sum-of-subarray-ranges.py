class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n, answer = len(nums), 0 
        stack = []

        # Process the minimum contribution
        for right in range(n):
            while stack and nums[stack[-1]] >= nums[right]:
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # Extra loop to process remaining elements in the stack for minimum
        while stack:
            mid = stack.pop()
            left = -1 if not stack else stack[-1]
            answer -= nums[mid] * (mid - left) * (n - mid)

        # Clear the stack to reuse it
        stack.clear()

        # Process the maximum contribution
        for right in range(n):
            while stack and nums[stack[-1]] <= nums[right]:
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # Extra loop to process remaining elements in the stack for maximum
        while stack:
            mid = stack.pop()
            left = -1 if not stack else stack[-1]
            answer += nums[mid] * (mid - left) * (n - mid)

        return answer
