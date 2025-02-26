class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        


        data = sorted(zip(timestamp, username, website))


        user_visits = defaultdict(list)

        for _ , user, website in data:
            user_visits[user].append(website)

        path = []
        def get_combinations(sites, n, i, out):
            if len(path) == n:
                out.append(tuple(path))
                return 
            
            
            for j in range(i, len(sites)):
                path.append(sites[j])
                get_combinations(sites, n,j+1, out)
                path.pop()
            
            


        pattern_visits = defaultdict(set)
        for user, sites in user_visits.items():
            patterns = []
            get_combinations(sites, 3, 0, patterns)
            for pattern in patterns:
                pattern_visits[pattern].add(user)

        max_pattern = None
        max_count = 0

        for pattern, users in pattern_visits.items():
            score = len(users)
            if score > max_count or (score == max_count and pattern < max_pattern):
                max_pattern = pattern
                max_count = score
        return list(max_pattern)