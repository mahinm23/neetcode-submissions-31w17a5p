class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = self.toDict(s)
        dict_t = self.toDict(t)

        if dict_s == dict_t:
            return True
        else:
            return False


    def toDict(self, s):
        ret_dict = {}

        for i in s:
            if i in ret_dict:
                ret_dict[i] += 1
            else:
                ret_dict[i] = 1

        return ret_dict