#!/usr/bin/python3

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        len_a = len(a)
        len_b = len(b)
        if len_b != len_a:
            return max(len_b, len_a)
        else:
            for i in range(len_a):
                if a[i] != b[i]:
                    return len_a
        return -1


if __name__ == "__main__":
     solution = Solution()
     value = solution.findLUSlength('aaa', 'bbb')
     print(value)
