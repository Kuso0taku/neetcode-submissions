class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {ch: 0 for ch in s}
        dictT = {ch: 0 for ch in t}

        for ch in s: dictS[ch] += 1
        for ch in t: dictT[ch] += 1
        
        if len(dictS.items()) != len(dictT.items()): return False
        for k,v in dictS.items():
            if k not in dictT.keys() or dictT[k] != v: return False
        return True