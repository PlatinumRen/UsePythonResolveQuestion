class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        lens = len(s)
        left_candle = [0] * lens
        right_candle = [0] * lens
        plates = [0] * lens
        plate = 0
        left_candle_index = 0

        for i in range(1, lens):
            if s[i - 1] == '*':
                plate += 1
            plates[i] = plate
            if s[i] == '|':
                left_candle_index = i
            left_candle[i] = left_candle_index

        right_candle_index = 0
        for i in range(lens - 2, -1, -1):
            if s[i] == '|':
                right_candle_index = i
            right_candle[i] = right_candle_index

        output = []
        for query in queries:
            left = query[0]
            right = query[1]
            if abs(left - right) <= 1:
                output.append(0)
                continue
            else:
                left, right = right_candle[left], left_candle[right]
                if left > right:
                    output.append(0)
                else:
                    output.append(plates[right] - plates[left])
        return output


if __name__ == '__main__':
    solution = Solution()
    print(solution.platesBetweenCandles('***|**|*****|**||**|*', [[1,17]]))
