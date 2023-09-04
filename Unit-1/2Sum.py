def twoSum(arr):
    return 0


def main():
    target = 9
    nums = [2,7,11,15]
    hashmap = dict()
    for i, num in enumerate(nums):
        print("i =",i)
        if num in hashmap:
            return [hashmap[num], i]

        hashmap[target-num] = i
main()