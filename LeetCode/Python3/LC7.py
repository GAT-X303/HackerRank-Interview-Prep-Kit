"""
LeetCode Problem - 7
Allan Hieng
"""

def reverseInt(x):
    numList = []
    output = ""
    negFlag = 0

    if x > (pow(2, 31)-1):
        return 0
    elif x < (pow(2, 31)*-1):
        return 0

    # checks if the original number was neg, if so it will account for it at the ned
    if x < 0:
        x = x*-1  # easier to work with pos numbers for now
        negFlag = 1  # used to distinguish

    # will keep going until the number is reduced via we have travelled every digit
    while x != 0:
        digit = int(x % 10)  # returns the LSD
        x = (x - digit)/10  # updates the current number we're working on
        numList.append(digit)  # add the digits to the list

    for i in range(len(numList)):
        # checks for the case where the first digit is 0
        # can only occur at i = 0
        if i == 0:
            if numList[i] == 0:
                None
            else:
                # if not 0 then just continue
                output = output + str(numList[i])
        else:
            output = output + str(numList[i])  # common case

    # converts the output into an into for output
    output = int(output)

    # handles the case of negs
    if negFlag:
        return output*-1

    return output
