class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_stack = []
        res =  [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while min_stack and temp > min_stack[-1][1]:
                index, pre_temp = min_stack.pop()
                res[index] = i - index

            min_stack.append((i, temp))
        
        return res