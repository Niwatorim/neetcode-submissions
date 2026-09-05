class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded+=i
            encoded+="/*,*/"
        return encoded
    def decode(self, s: str) -> List[str]:
        return[i for i in s.split("/*,*/")[:-1]]