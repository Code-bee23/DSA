import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #create project:(capital required,profit)
        projects=[]
        
        for i in range(len(profits)):
            projects.append((capital[i], profits[i]))

        #sort the project by vapital
        projects.sort()
        
        #max heap for profits
        max_heap = []
        i = 0
        #we can select at most k projects
        for _ in range(k):
           
           #add all  the projects we can currently afford
            while i<len(projects) and projects[i][0]<=w:
                
                profit = projects[i][1]
                
                #python only has min heap
                # so for max heap negative value of profit we take
                heapq.heappush(max_heap,-profit)

                i += 1
            
            #if no project is affordable
            if not max_heap:
                break
            
            # take project with maximum profit
            profit = -heapq.heappop(max_heap)
            
            #increase the money
            w += profit

        return w
