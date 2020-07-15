#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jodeb
#
# Created:     10/07/2020
# Copyright:   (c) jodeb 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
##name has [prefix and midname  ], [prefix or middlename ] [prefix and designation] or [prefix and middlename and designation]

prefixeslist=['sleva','anga','aera','ilga','yuga','yukya','yuktari', "fen",
"swetzer", "angli", "swana", 'do']
middlenameslist=['neva','yuva','star','landi', "seg", "sigh", "zerle",
"sethio", "dambia",'talia', 'burgh', 'avla', 'stelba',]

designationlist=['land', " Republic",   " Fedaration", " Conglomerete", " Empire",
" Kingdom"]

def randfinder(lenvar):

    return random.randrange(0,lenvar)


def randnamegen():
    xstr = (prefixeslist[randfinder(len(prefixeslist))])
    nextcombo = random.randint(0,7)
    if nextcombo <= 2:
        ##name just includes prefix and designation
        mstr = designationlist[randfinder(len(designationlist))]
        laststr = ""
    elif nextcombo == 3:
        ###name includes prefix, middle name, and designation
        mstr = middlenameslist[randfinder(len(middlenameslist))]
        laststr = designationlist[randfinder(len(designationlist))]

    elif nextcombo > 3:
        mstr=""
        laststr=middlenameslist[randfinder(len(middlenameslist))]


    countryname = xstr+mstr+laststr
    print(countryname)



randnamegen()


