def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


S = input('S = ')
if isPalindrome(S):
    print('회문입니다.')
else:
    print('회문이 아닙니다.')
