#
# @lc app=leetcode.cn id=707 lang=python3
# @lcpr version=30204
#
# [707] 设计链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next



class MyLinkedList:
    
#["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
#' +
# '[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]] 


    def __init__(self):
        self.head = ListNode()
        self.lenth = 0

    def get(self, index: int) -> int:
        now = self.head
        while now!=None:
            print(now.val)
            now = now.next
        if index > self.lenth - 1 or index < 0:
            return -1
        current = self.head.next
        while index:
            current = current.next
            index -= 1
        return current.val
            

    def addAtHead(self, val: int) -> None:
        self.head.next = ListNode(val, self.head.next)
        self.lenth += 1


    def addAtTail(self, val: int) -> None:
        current = self.head
        while current.next!= None:
            current = current.next
        current.next = ListNode(val)
        self.lenth += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.lenth:
            current = self.head
            while index:
                current = current.next
                index -= 1
            next = current.next
            current.next = ListNode(val)
            current.next.next = next
            self.lenth += 1

    def deleteAtIndex(self, index: int) -> None:
        if index <= self.lenth - 1:
            current = self.head
            while index:
                current = current.next
                index -= 1
            next = current.next.next
            current.next = next
            self.lenth -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end



