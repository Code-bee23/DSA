class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        res = []
        def check(idx,diary,sum):
            if sum == target:
                res.append(diary.copy())
                return

            if idx == n or sum > target:
                return
                    
            check(idx+1,diary,sum)

            if candidates[idx] + sum <= target:
                diary.append(candidates[idx])

                check(idx,diary,sum +  candidates[idx])

                diary.pop()

        check(0,[],0)

        return res