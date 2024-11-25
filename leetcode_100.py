class Solution:
    def isSameTree(self, p, q):
        #  設定第一種終止條件：就是當p,q為空樹
        if p is None and q is None:
            return True
        #  設定第二種終止條件，其中一個是空的另一個不是，很明顯就不是一樣的
        if p is None or q is None:
            return False
        #  開始遞迴，當相同位置一樣，就會持續到結束
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # 就是當p的某一個位置不等於q的同一個位置，就會回傳下面的False
        return False