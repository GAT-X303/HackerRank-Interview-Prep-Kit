"""
LeetCode Problem - 9
Allan Hieng
"""

def isPalindrome(x):
    if x < 0:
        return False

    #really stupid way of doing this, almost too easy
    stringX = str(x)
    reverseX = stringX[::-1]
    if stringX == reverseX:
        return True     

    numList = []
    numListLength = 0

    while x > 0:
        remainder = int(x%10)
        x = int((x - remainder)/10)
        numList.append(remainder)
        numListLength = numListLength + 1
    

    