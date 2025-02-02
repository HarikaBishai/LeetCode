class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)

        for account in accounts:
            accountFirstEmail = account[1]
            if accountFirstEmail not in graph:
                graph[accountFirstEmail] = []
            for i in range(2, len(account)):
                graph[accountFirstEmail].append(account[i])
                graph[account[i]].append(accountFirstEmail)


        visited = set()
        def dfs(email, out):
            visited.add(email)
            out.append(email)
            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, out)
                
        merged = []
        for account in accounts:
            accountName = account[0]
            accountFirstEmail = account[1]
            if accountFirstEmail not in visited:
                emails = [] 
                dfs(accountFirstEmail, emails)
                emails.sort()
                merged.append([accountName]+ emails)
            
        return merged
                
        
        


                
                
               
            







        