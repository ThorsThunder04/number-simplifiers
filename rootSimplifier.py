
def squareRoot(num, string=False):

    if (int(num**0.5) == float(num**0.5)): # returns the square root of the number if it is a simple root.
        return int(num ** 0.5)
    
    tempDivided = num # will hold the number that will be devided multiple times.
    # multCounts = [] # holds the numbers that are squarable
    currentHighest = 1 # holds the highest square
    lowestRemainingRoot = 1
    simplifiable = None

    for div in range(2, num): # iterates through numbers to find squares in the square root.
        if ((tempDivided % div) == 0) and ((tempDivided/div % div) == 0):
            currentHighest = div # saves the highest found square that will multiply the root.
            lowestRemainingRoot = int((tempDivided/div)/div) # gets a value of the smallest remaining root after it finds the squares.
            simplifiable = True # so that th function knows if the number can be simplified and which one to return at the end.

        else:
            continue

    if (string): # for it to be displayed as a string
        if (simplifiable):
            return str(currentHighest) + '*sqrt(' + str(lowestRemainingRoot) + ')'
        else:
            return 'sqrt(' + str(num) + ')'
    
    else: # just return the results
        if (simplifiable):
            return currentHighest, lowestRemainingRoot
        else:
            return [num] # if the returned type is list, then it means that it's the ireductable number, and not a number like sqrt(16) -> 4
