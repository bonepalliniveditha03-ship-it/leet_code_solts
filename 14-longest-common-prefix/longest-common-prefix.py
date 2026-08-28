class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i in range(len(strs[0])):
            ch = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != ch:
                    return ans

            ans += ch

        return ans
        