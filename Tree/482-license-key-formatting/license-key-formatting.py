class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-", '')
        
        if len(s) < k:
            return s.upper()
        
        first_group_len = len(s)%k if len(s)%k > 0 else k
        first_group = s[:first_group_len].upper()
        remaining_groups =  [s[i:i+k].upper()  for i in range(first_group_len, len(s), k)]
        
        return "-".join([first_group] + remaining_groups)
        