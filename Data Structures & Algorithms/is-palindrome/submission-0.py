class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        pointer 1 and pointer -1
        case insensitize
        """
        pointer = -1
        last = 0
        new_s="".join(filter(str.isalnum,s))
        for i in new_s:
            pointer +=1
            last-=1
            if pointer == last:
                break
            if new_s[pointer].lower() == new_s[last].lower():
                continue
            else:
                return False
        return True
