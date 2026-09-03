class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for t in range (len(temperatures)):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = t - prev_index 
            stack.append(t)

        return result

