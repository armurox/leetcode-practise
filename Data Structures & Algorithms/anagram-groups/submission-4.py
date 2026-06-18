class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(str1: str, str2: str) -> bool:
            if (length := len(str1)) != len(str2):
                return False
            count_1, count_2 = {}, {}
            for i in range(length):
                count_1[str1[i]] = 1 + count_1.get(str1[i], 0)
                count_2[str2[i]] = 1 + count_2.get(str2[i], 0)
            for key in count_1:
                if count_1[key] != count_2.get(key, 0):
                    return False
            return True
        
        final_result = []
        found_anagrams = set()
        for i in range(len(strs)):
            temp_result = []
            if strs[i] in found_anagrams:
                continue
            for j in range(i + 1, len(strs)):
                if isAnagram(strs[i], strs[j]):
                    if strs[i] in temp_result:
                        temp_result.append(strs[j])
                    else:
                        temp_result.append(strs[i])
                        temp_result.append(strs[j])
            if temp_result == []:
                final_result.append([strs[i]])
            else:
                final_result.append(temp_result)
            found_anagrams = found_anagrams.union(temp_result)
        return final_result
            
