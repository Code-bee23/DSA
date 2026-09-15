import heapq

class Solution:
    def kthSmallest(self, matrix, k):

        n = len(matrix)

        min_heap = []

        # Put first element of every row into heap
        for row in range(n):
            heapq.heappush(
                min_heap,
                (matrix[row][0], row, 0)
            )

        # Find kth smallest element
        for _ in range(k):

            value, row, col = heapq.heappop(min_heap)

            # Move to next element in the same row
            if col + 1 < n:

                next_value = matrix[row][col + 1]

                heapq.heappush(
                    min_heap,
                    (next_value, row, col + 1)
                )

        return value