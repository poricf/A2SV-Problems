# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # insert between 2 nodes the greatest common divisor of them
        def findGreatestCommonDivisor(num1, num2):
            if num2 == 0:
                return num1
            if num1 == 0:
                return num2

            remainderList = [num2]
            divisor, remainder = num1, num2
            while remainder != 0:
                temp = remainder
                remainder = divisor % remainder
                remainderList.append(remainder)
                divisor = temp
            return remainderList[-2]
        
            
        temp = head
        while temp and temp.next:
            GCD = findGreatestCommonDivisor(temp.val, temp.next.val)
            newNode = ListNode(GCD)
            nextTemp = temp.next
            temp.next = newNode
            newNode.next = nextTemp
            temp = nextTemp
        return head            