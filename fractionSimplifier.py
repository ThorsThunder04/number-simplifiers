def simplifyFraction(nom, denom, string=False):
    
    nomMults = [i for i in range(1,abs(nom)+1) if (nom % i) == 0] # generates a list of whole multiples for the nominator
    denomMults = [i for i in range(1,abs(nom)+1) if (denom % i) == 0] # generates a list of whole multiples for the denominator

    hasCommonMult = None # for the conditional at the end
    commonMult = 1

    for i in range(1, len(nomMults)+1): # iterates through the lits to look for the highest common multiple
        if (nomMults[-i] in denomMults):
            commonMult = nomMults[-i]
            hasCommonMult = True
            break
    # returns the simplified (or not) values in a tuble so it can be used later on.
    
    if (string): # gives the option to be returned in a string form.
        if (hasCommonMult):
            if (denom/commonMult == 1): # check to see if it can be returned in a non fraction form
                return str(int(nom/commonMult))

            elif (denom/commonMult == -1): # returns as non fraction if denominator is negative
                return str(int(-nom/commonMult))
            
            elif (nom/commonMult < 0) and (denom/commonMult < 0): # inverts both signs if it's -x/-y
                return str(int(-nom/commonMult)) + '/' + str(int(-denom/commonMult))

            else: # returns in a simplified fraction form
                return str(int(nom/commonMult)) + '/' + str(int(denom/commonMult))

    else: # returns in tuple form
        if (hasCommonMult):
            if (denom/commonMult == 1): # check to see if it can be returned in a non fraction form
                return int(nom/commonMult)

            elif (denom/commonMult == -1): # so that negative divition can also be returned in a non fraction form.
                return int(-nom/commonMult)
            elif (nom/commonMult < 0) and (denom/commonMult < 0):
                return int(-nom/commonMult), int(-denom/commonMult)
            else:
                return (int(nom/commonMult), int(denom/commonMult))
