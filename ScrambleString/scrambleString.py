class Solution:

    memo = {}

    def check(self, s1: str, s2: str) -> bool:
        assert len(s1) == len(s2)
        n = len(s1)
        if n == 1:
            return s1 == s2
        elif n == 2:
            return s1 == s2 or s1 == s2[::-1]
        else:
            if s1 == s2 or s1 == s2[::-1]:
                self.memo[(s1, s2)] = True
                return True

            if (s1, s2) in self.memo:
                return self.memo[(s1, s2)]
            else:
                if sorted(s1) != sorted(s2):
                    self.memo[(s1, s2)] = False
                    return False

                for position in range(1, n):
                    s1_left, s1_right = s1[:position], s1[position:]
                    s2_left, s2_right = s2[:position], s2[position:]
                    s3_left, s3_right = s2[-position:], s2[:-position]

                    if self.check(s1_left, s2_left) and self.check(s1_right, s2_right):
                        self.memo[(s1, s2)] = True
                        return True
                    elif self.check(s1_left, s3_left) and self.check(s1_right, s3_right):
                        self.memo[(s1, s2)] = True
                        return True
                else:
                    self.memo[(s1, s2)] = False
                    return False

    def isScramble(self, s1: str, s2: str) -> bool:
        return self.check(s1, s2)