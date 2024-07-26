def permutation(ip, op, res):
    if len(ip) == 0:
        res.append(op)
        return 

    op1 = op + ip[0]
    op2 = op + ip[0] + ' '

    ip1 = ip[1:]

    if len(ip1) > 0:
        permutation(ip1, op1, res)
        permutation(ip1, op2, res)
    else:
        permutation(ip1, op1, res)

    return res

print(permutation("ABC", "", []))

def permutationCaseChange(ip,op,res):
    if len(ip) == 0:
        res.append(op)
        return 
    
    op1 = op + ip[0]
    op2 = op + ip[0].upper()
    ip1 = ip[1:]
    permutationCaseChange(ip1,op1,res)
    permutationCaseChange(ip1,op2,res)
    
    return res

print(permutationCaseChange("ab","",[]))
    
class Solution:
    def letterCasePermutation(self, s: str):
        def PermutationLetterChange(ip,op,res):
            if len(ip) == 0:
                res.append(op)
                return

            op1 = op + ip[0].lower() 
            op2 = op + ip[0].upper() 
            ip1 = ip[1:]

            PermutationLetterChange(ip1,op1,res)
            if ip[0].isalpha():
                PermutationLetterChange(ip1,op2,res)

            return res

        return PermutationLetterChange(s,"",[])


sol = Solution()
print(sol.letterCasePermutation("a1b2"))