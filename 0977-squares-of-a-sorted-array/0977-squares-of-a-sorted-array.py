class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pos = []
        neg = []

        #separate neg. and positive number
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)

        #Case1: when no negative number comes
        if len(neg) == 0:
            return [x*x for x in pos]

        #case2: when no positive number comes
        if len(pos) == 0:
            res = [x*x for x in neg]
            res.reverse()
            return res

        #Case3: when both are present:
        neg = [x*x for x in neg][::-1]
        pos = [x*x for x in pos]

        n, m = len(neg) , len(pos)

        res = []
        i = j = 0 
        while i<n and j<m :
            if neg[i] < pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1

        while i<n :
            res.append(neg[i])
            i += 1
        while j<m :
            res.append(pos[j])
            j += 1
        return res

