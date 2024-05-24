# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.maxx = 0
        
    def build_trie(self, num):
        curr = self.root

        for i in range(32,-1,-1):
            bit = 1 if num & (1 << i) else 0
            if not curr.children[bit]:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]

    def find_max(self,num):
        curr = self.root
        ans = 0

        for i in range(32,-1,-1):
            bit = 1 if num & (1 << i) else 0
            if curr.children[1-bit]:
                ans = ans | (1<<i)
                curr = curr.children[1-bit]
            else:       
                curr = curr.children[bit]

        self.maxx = max(self.maxx, ans)


    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.build_trie(num)

        for num in nums:
            self.find_max(num)

        return self.maxx