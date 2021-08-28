class Solution:
    def climbStairs(self, n: int) -> int:
        # shorthand
        # n=1 => 1
        # n=2 => 2
        # n=3 => 3
        # n=4 => 5
        # n = 4
        # 1 + 1 + 1 + 1
        # 1 + 1 + 2
        # 1 + 2 + 1
        # 2 + 1 + 1
        # 2 + 2
        # === 5 ways
        # n = 5
        # 1 + 1 + 1 + 1 + 1
        # 1 + 1 + 1 + 2
        # 1 + 1 + 2 + 1
        # 1 + 2 + 1 + 1
        # 2 + 1 + 1 + 1
        # 2 + 2 + 1
        # 2 + 1 + 2
        # 1 + 2 + 2
        # === 8 ways
        if n == 1 or n == 2 or n == 3:
            return n
        
        # Exceed time limit with recursion sadly
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        sum = 0
        previous = 3
        pre_previous = 2
        for i in range(4, n+1):
            sum = previous + pre_previous
            previous, pre_previous = sum, previous
        return sum


        
        
        # d = {2: 2, 3: 3}
        # for i in range(4, n+1):
        #     d[i] = d.get(i-1) + d.get(i-2)
        # return d.get(n)
        # Slightly faster and also allows you to have all the previous values stored
        # So if you wanted to remove other valeus you dont need to run everything again
        # I don't like this solution tho, as it's not as clear as the one above