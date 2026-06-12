class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for idx, item in enumerate(strs):
            item = self.freq_list(item)
            if item not in grouped_anagrams:
                grouped_anagrams[item] = []

                grouped_anagrams[item].append(strs[idx])
            else:
                grouped_anagrams[item].append(strs[idx])

        return list(grouped_anagrams.values())


    def freq_list(self, word):
        ret_arr = [0]*26
        for char in word:
            char = char.lower()
            ret_arr[ord(char) - ord('a')] += 1
        return tuple(ret_arr)
