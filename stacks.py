# stacks are basically arrays

arr= [1,2,3,4,6,7,3,5]

for i in arr:
    print(i)

# remember you cannot use pop with (for i in arr)
print("using pop")
for i in range(len(arr)):
    print(i)
    print(arr.pop())


arr2= [1,2,3,4,6,7,3,5]
print("inserting into arr2")
arr2.insert(1,
            7)
print(arr2)


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index
        result = []

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                result.append([prevMap[diff],i])
            prevMap[n] = i
        return result

sol = Solution()
resultz = sol.twoSum([2,7,3,3,6,15],6)
print(resultz)