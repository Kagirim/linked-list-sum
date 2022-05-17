class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        self.carry_val = 0
        self.sum_val = 0
        count = 0
        while l1 or l2 is not None:
            count += 1
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            l1.val += self.carry_val
            llst1_val = l1.val
            llst2_val = l2.val
            self.sum_val = (llst1_val + llst2_val) % 10
            self.carry_val = (llst1_val + llst2_val) // 10
            globals()[f'sum_node{count}'] = ListNode(self.sum_val)
            try:
                globals()[f'sum_node{count - 1}'].next = globals()[f'sum_node{count}']
            except KeyError:
                globals()[f'sum_node{count}'].next = ListNode(self.sum_val)

            l1 = l1.next
            l2 = l2.next
        if self.carry_val > 0:
            globals()[f'sum_node{count + 1}'] = ListNode(self.carry_val)
            globals()[f'sum_node{count}'].next = globals()[f'sum_node{count + 1}']
        return sum_node1


l1 = [2, 4, 9]
l2 = [5, 6, 4, 9]

for i in range(0, len(l1)):
    if i == 0:
        lst1node0 = ListNode(l1[i])
        globals()[f'lst1node{i + 1}'] = ListNode(l1[i + 1])
        globals()[f'lst1node{i}'].next = globals()[f'lst1node{i + 1}']
    if 0 < i < len(l1) - 1:
        globals()[f'lst1node{i + 1}'] = ListNode(l1[i + 1])
        globals()[f'lst1node{i}'].next = globals()[f'lst1node{i + 1}']
    elif i == len(l1) - 1:
        continue

for i in range(0, len(l2)):
    if i == 0:
        lst2node0 = ListNode(l2[i])
        globals()[f'lst2node{i + 1}'] = ListNode(l2[i + 1])
        globals()[f'lst2node{i}'].next = globals()[f'lst2node{i + 1}']
    if 0 < i < len(l2) - 1:
        globals()[f'lst2node{i + 1}'] = ListNode(l2[i + 1])
        globals()[f'lst2node{i}'].next = globals()[f'lst2node{i + 1}']
    elif i == len(l2) - 1:
        continue

s = Solution()
s.addTwoNumbers(lst1node0, lst2node0)
