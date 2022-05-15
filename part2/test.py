import time

def logging_time(origin_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = origin_fn(*args, **kwargs)
        end_time = time.time()

        print("Working time [{}] : {} sec".format(origin_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn


#두 수의 합
#1.1 브루트 포스로 계산

@logging_time
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

#in을 이용한 탐색
@logging_time
def twoSum2(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

#첫 번째 수를 뺀 결과 키 조회
@logging_time
def twoSum3(nums: list[int], target: int) -> list[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i
    
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


#조회 구조 개선
@logging_time
def twoSum4(nums: list[int], target: int) -> list[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        
        nums_map[num] = i

#투 포인터 이용
@logging_time
def twoSum5(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
            

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("result : ",twoSum(nums, target))
    print("result : ",twoSum2(nums, target))
    print("result : ",twoSum3(nums, target))
    print("result : ",twoSum4(nums, target))