from collections import defaultdict

class Solution:
    def maximumSum(self, nums: list[int]) -> int:

        def find_sum_of_digits(num):
            ans = 0
            while num != 0:
                ans += num % 10
                num = num // 10
            return ans

        nums.sort(reverse=True)
        counts = defaultdict(list)

        for num in nums:
            counts[find_sum_of_digits(num)].append(num)

        ans = -1

        for key in counts:
            if len(counts[key]) > 1:
                temp = counts[key][0] + counts[key][1]
                if temp > ans:
                    ans = temp

        return ans

solution = Solution()
nums = [229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]
print(solution.maximumSum(nums))
