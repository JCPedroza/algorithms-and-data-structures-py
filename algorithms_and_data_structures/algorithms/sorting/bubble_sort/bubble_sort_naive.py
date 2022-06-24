def bubble_sort(nums: list[float]) -> list[float]:
    for _ in range(len(nums)):
        for indx in range(len(nums) - 1):
            if nums[indx] > nums[indx + 1]:
                nums[indx], nums[indx + 1] = nums[indx + 1], nums[indx]

    return nums


algorithm = bubble_sort
name = "naive"
