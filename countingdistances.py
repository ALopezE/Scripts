#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      albertolopez
#
# Created:     30/01/2014
# Copyright:   (c) albertolopez 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

### this script counts the number of genes which are at distance 0, 10<kb and  3<kb
## There are 8 files: UBG_BRAIN_STAMPY,FBG_MBG_BRAIN_STAMPY, UBG_BRAIN_NGM, FBG_MBG_BRAIN_NGM
##  UBG_malphigian_STAMPY,FBG_MBG_mapphigian_STAMPY, UBG_malphigian_NGM, FBG_MBG_malphigian_NGM
## for each file at at time giving the file name it creates a dictionary with all the columns that can be accessed
## Loop over the columns corresponding to the distances to p_mle, p_fas, p_msl, p_msl2, p_msl3 and prints the distances to the screen

import sys

with open('C:/Users/albertolopez/Desktop/python/STAMPY_MT_MBG_FORPYTHONSCRIPT.csv', 'r') as infile:
    header = infile.readline()
    col_values = {var:[] for var in header.split()}
    var_idx_dict = {idx:var for idx,var in enumerate(header.split())}

    for line in infile:
        values = line.split('\t')

        for idx,value in enumerate(values):
            var = var_idx_dict[idx]
            col_values [var].append(value)
sumnullmle= 0
summiddlemle = 0
sumsmallmle=0
dif1= 0
try:
    for element in col_values["p_mle"]:
      if int(element) == 0:
        sumnullmle = sumnullmle + 1
      elif int(element) < 3000:
        sumsmallmle = sumsmallmle + 1
        continue
      elif int(element) > 3000 and (int(element)  < 10000):
        summiddlemle = summiddlemle + 1
      else:
       dif1 = dif1 + 1
except:
    pass

sumnullhas = 0
summiddlehas = 0
sumsmallhas= 0
dif2 = 0
try:
    for element in col_values["p_has"]:
     if int(element) == 0:
            sumnullhas = sumnullhas + 1
     elif int(element) < 3000:
        sumsmallhas = sumsmallhas + 1
     elif int(element) > 3000 and (int(element)  < 10000):
        summiddlehas = summiddlehas + 1
     else:
        dif2 = dif2 +1
except:
     pass
sumnullmsl = 0
summiddlemsl = 0
sumsmallmsl= 0
dif3= 0
try:
    for element in col_values["p_msl"]:
     if  int(element) == 0:
        sumnullmsl = sumnullmsl + 1
     elif int(element) < 3000:
        sumsmallmsl = sumsmallmsl + 1
     elif int(element) > 3000 and (int(element)  < 10000):
        summiddlemsl = summiddlemsl + 1
     else:
        dif3= dif3 + 1
except:
   pass

sumnullmsl2 = 0
summiddlemsl2 = 0
sumsmallmsl2= 0
dif4 = 0
try:
    for element in col_values["p_msl2"]:
     if int(element) == 0:
        sumnullmsl2 = sumnullmsl2 + 1
     elif int(element) < 3000:
        sumsmallmsl2 = sumsmallmsl + 1
     elif int(element) > 3000 and (int(element)  < 10000):
        summiddlemsl2 = summiddlemsl2 + 1
     else:
        dif4 = dif4 + 1
except:
    pass
sumnullmsl3 = 0
summiddlemsl3 = 0
sumsmallmsl3 = 0
dif5= 0
try:

    for element in col_values["p_msl3"]:
     if int(element) == 0:
        sumnullmsl3 = sumnullmsl3 + 1
     elif int(element) < 3000:
        sumsmallmsl3 = sumsmallmsl3 + 1
     elif int(element) > 3000 and (int(element) < 10000):
        summiddlemsl3 = summiddlemsl3 + 1
     else:
        dif5 = dif5 + 1
except:
    pass

print" MLE\n"
print "Number of counts equal 0 in: ", sumnullmle
print "Number of counts between 3000 and 10000:", summiddlemle
print "Number of counts smaller than 3000: ", sumsmallmle
print "Rest,further than 10000", dif1
print "HAS\n"
print "Number of counts equal 0: ", sumnullhas
print "Number of counts between 3000 and 10000:", summiddlehas
print "Number of counts smaller than 3000: ", sumsmallhas
print "Rest,further than 10000", dif2
print "MSL\n"
print "Number of counts equal 0: ", sumnullmsl
print "Number of counts between 3000 and 10000:", summiddlemsl
print "Number of counts smaller than 3000: ", sumsmallmsl
print "Rest,further than 10000", dif3
print "MSL2\n"
print "Number of counts equal 0: ", sumnullmsl2
print "Number of counts between 3000 and 10000:", summiddlemsl2
print "Number of counts smaller than 3000: ", sumsmallmsl2
print "Rest, meaning further than 10000", dif4
print "MSL3\n"
print "Number of counts equal 0: ", sumnullmsl3
print "Number of counts between 3000 and 10000:", summiddlemsl3
print "Number of counts smaller than 3000: ", sumsmallmsl3
print "Rest, further than 10000", dif5








