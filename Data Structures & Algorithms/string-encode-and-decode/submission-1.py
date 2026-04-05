class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for string in strs:
            res.append(str(len(string)) + '#' + string)
        
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        cnt = 0
        string = ""
        res = []
        inString = False

        for ch in s:
            if not inString:
                if ch.isdigit():
                    cnt = cnt*10 + int(ch)
                elif ch == '#':
                    inString = True

                    if cnt == 0:
                        res.append("") 
                        inString = False
            else:
                string += ch
                cnt -= 1

                if cnt == 0:
                    inString = False
                    res.append(string)
                    string = ""
        

        return res
