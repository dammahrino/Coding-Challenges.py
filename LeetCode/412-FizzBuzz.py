# Problem Description
# https://leetcode.com/problems/fizz-buzz

# Input: n = 3
# Output: ["1","2","Fizz"]

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        output = []
        for currentValue in range(1, n + 1):
            if currentValue % 3 == 0 and currentValue % 5 == 0:
                output.append("FizzBuzz")
            elif currentValue % 3 == 0:
                output.append("Fizz")
            elif currentValue % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(currentValue))
            
        return output


print(f'Input: 3 | Expected output: ["1","2","Fizz"] | Received expected output? {Solution().fizzBuzz(3) == ["1","2","Fizz"]}')