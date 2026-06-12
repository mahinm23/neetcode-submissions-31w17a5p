class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for idx, item in enumerate(strs):
            item = self.freq_list(item)
            if item in anagram_dict:
                anagram_dict[item].append(strs[idx])
            else:
                anagram_dict[item] = []
                anagram_dict[item].append(strs[idx])

        print(anagram_dict)
        return list(anagram_dict.values())

    def freq_list(self, word):
        ret_arr = [0]*26
        for char in word:
            char = char.lower()
            ret_arr[ord(char)-ord('a')] += 1
        return tuple(ret_arr)