def bubble_sort(nums: list[float]) -> list[float]:
    is_sorted = True

    for loop in range(len(nums) - 1):
        for indx in range(len(nums) - loop - 1):
            if nums[indx] > nums[indx + 1]:
                is_sorted = False
                nums[indx], nums[indx + 1] = nums[indx + 1], nums[indx]

        if is_sorted:
            break

    return nums


algorithm = bubble_sort
name = 'optimized'
