class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = self.str_to_dict(s)
        dict_t = self.str_to_dict(t)

        if dict_s == dict_t:
            return True
        else:
            return False



    def str_to_dict(self, word):
        ret_dict = {}
        for i in word:
            if i not in ret_dict:
                ret_dict[i] = 1
            else:
                ret_dict[i] += 1
        return ret_dict
        