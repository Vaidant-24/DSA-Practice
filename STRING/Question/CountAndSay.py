class Solution:
    def countAndSay(self, n: int) -> str:
        def gen(s):
            s = str(n)
            hash = set()
            ans = ''
            for i in range(len(s)):
                cnt = 0
                if s[i] not in hash:
                    for j in range(i,len(s)):
                        if s[i] == s[j]:
                            cnt += 1
                    ans = ans + str(cnt)+ s[i]
                    hash.add(s[i])
            return ans
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        ans = gen(s)
        return ans

def gent(s):
    hash = set()
    ans = ''
    for i in range(len(s)):
        cnt = 0
        if s[i] not in hash:
            for j in range(i,len(s)):
                if s[i] == s[j]:
                    cnt += 1
                    ans = ans + str(cnt)+ s[i]
                    hash.add(s[i])
    return ans
print(gent("11"))