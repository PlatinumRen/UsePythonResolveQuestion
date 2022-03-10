class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        lens = len(nums)
        rotation_count = [0]*lens

        for index, num in enumerate(nums):
            start = index + 1
            if start >= lens:
                rotation_count[start - lens] += 1
            else:
                rotation_count[start] += 1
            
            end = (lens + index - num + 1) % lens
            rotation_count[end] -= 1
        
        min_locate = lens
        max_value = 0
        value = 0

        for index, rotation in enumerate(rotation_count):
            value += rotation
            if value > max_value:
                max_value = value
                min_locate = index
            elif value == max_value:
                if index < min_locate:
                    min_locate = index
        
        return min_locate
