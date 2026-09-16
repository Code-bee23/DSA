from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        
        #max heap
        pq = []
        for count in freq.values():
            heapq.heappush(pq,-count)

        time = 0

        while pq:

            temp = []

            #one cycle has n+1 position 
            for _ in range(n+1):

                if pq:
                    count = heapq.heappop(pq)

                    count+=1

                    if count != 0:
                        temp.append(count)

                time += 1

                #if no task remains anywhere
                if not pq and not temp:
                    break
                    
            #put remaining tasks back
            for count in temp:
                heapq.heappush(pq,count)

        return time