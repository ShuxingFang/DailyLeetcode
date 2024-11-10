class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        for c in magazine:
            count[ord(c) - ord('a')] += 1

        for c in ransomNote:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                return False

        return True



# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         note_dict = defaultdict(int)
#         magazine_dict = defaultdict(int)

#         for c in ransomNote:
#             note_dict[c] += 1

#         for c in magazine:
#             magazine_dict[c] += 1

#         for key in note_dict:
#             if note_dict[key] > magazine_dict[key]:
#                 return False

#         return True

ransomNote = "aa"
magazine = "aab"
solution = Solution()
print(solution.canConstruct(ransomNote, magazine))
