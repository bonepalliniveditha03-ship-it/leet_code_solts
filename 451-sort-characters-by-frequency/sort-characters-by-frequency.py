class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        result = ""
        for ch in sorted(d, key=d.get, reverse=True):
            result += ch * d[ch]
        return result