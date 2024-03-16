from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_set = defaultdict(int)
        l, max_length = 0, 0
        out_string  = ''
        for r in range(len(s)):
            if not s[r] in char_set:
                while len(char_set) == 2:
                    char_set[s[l]]-=1
                    if char_set[s[l]] <= 0:
                       char_set.pop(s[l])
                    l+=1     
            char_set[s[r]] +=1
            if r-l+1 > max_length:
                out_string = s[l: r+1]
                max_length = r-l+1

        return out_string

def main():
    s = input("Enter the string: ")
    solution = Solution()
    print(solution.lengthOfLongestSubstringTwoDistinct(s.strip()))

if __name__ == "__main__":
    main()
