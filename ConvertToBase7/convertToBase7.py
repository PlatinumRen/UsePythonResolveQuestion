class Solution:
    def convertToBase7(self, num: int) -> str:
        signal = ''
        if num < 0:
            num = -num
            signal = '-'

        output_list = []
        while num >= 7:
            a, b = num.__divmod__(7)
            num = a
            output_list.append(str(b))
        output_list.append(str(num))

        output = signal + ''.join(output_list[::-1])
        return output


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToBase7(-222))

