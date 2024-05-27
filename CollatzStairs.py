##########################################################################
#  (c) Copyright 2024 - Ali Ebnenasir
# 
#  Protected by GNU GPL v3.0  https://www.gnu.org/licenses/gpl-3.0.en.html 
# 
# This program is an implementation of the algorithm in 
# for the generation of Collatz numbers in a specific stair j, for j >0.  
# The j-th stait includes all natural values from where the set of powers
# of two can be reach in exactly j application of Collatz function.
# The Collatz function is defined over positive integers as follows:
#  if n is odd, then C(n) = 3n+1
#  if n is even, then C(n) = n/2
#
# 
# Disclaimer of Warranty:
# THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY 
# APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT 
# HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT 
# WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT 
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
# FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND 
# PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE 
# DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR 
# OR CORRECTION.
##########################################################################
import sys
import math

mlist=[]  # declare a list of integers


def verify(x: int, s: str) -> bool:
    arr=s
    orgX = x

    if ((x < 1) or not(str(float(x)).endswith('.0')) ) : return False     
    
    if str(float(x)).endswith('.0'):
        if (str(math.log(x,2)).endswith('.0')):
         #   print("Verify: ", x, " is a power of 2!")
            return False
    else:
      #  print("Verify: ", x, " is not an integer!")
        return False

   # for t in range(len(arr)-1, -1, -1): print("Bit", t, "is ", arr[t])

                

    for i in range(len(arr)-1, -1, -1): # scan from lsb to msb
       # print("Here is the bit value of arr[i] ", int(arr[i]))
        if (int(arr[i]) == 1): y = 3*x + 1
        else: y = x/2

        if ((int(arr[i]) == 1) or (int(arr[i]) == 0)):
            # start the verification here
            if str(float(y)).endswith('.0') and (y >= 1):
                if (str(math.log(y,2)).endswith('.0')):
               #     print("Verify: ", y, " is a power of 2 while verifying ", orgX)
                    return False
                else:
                    if (int(arr[i]) == 1) and (y %2 !=0) and (x %2 ==0):
                #        print("Verify: y = ", y, "is odd and x =", x," is even while verifying ", orgX, "!")
                        return False    
            else:
               # print("Verify: y =", y, " is non-integer for x =", x)
                return False
        else:
           # print("Verify: Unknown character in the string ", s)
            return False
        x = y
    return True
    

# This is a function for a nested for-loop with variable depth n. 
def  recursiveFor(n: int, l: int, origN:int, j: int, qj: int, Y_k: int):
    if (n > 1):   # skip the last loop; leave it for termination
        for x in range(0,l+1)[::-1]:
            mlist.append(x)
            recursiveFor(n-1,l, origN, j, qj, Y_k)
            mlist.pop(origN - n)
    else:
#        accept = True
        for x in range(0,l+1)[::-1]: 
            mlist.append(x)
#            print(mlist);
#            mlist.pop()
            accept = True
            for i in range(0,origN-1): 
                if (mlist[i] < mlist[i+1]):
                    accept = False;
                    break;
            if (accept == True):
             #   print(mlist); # ordering of m[] is non-increasing.
                sum = 0
                for i in range(0,origN):
                    sum = sum + math.pow(2,mlist[i]) * math.pow(3,i+1)
                collatzNum = ((math.pow(2,j-qj) * Y_k) - sum) / math.pow(3,qj)
               # print("Collatz number: ", collatzNum)
                binStr = ""
                for i in range(0,len(mlist))[::-1]:
                  #  print("i= ", i, "mlist[i]= ", mlist[i])
                    if (mlist[i] == 0):
                        binStr = "1" + binStr 
                    else:
                        if (i == (len(mlist) -1) ):
                            for t in range(0,mlist[i]): binStr = "0" + binStr
                            binStr =  "1" + binStr
                        else:
                            if (mlist[i]== mlist[i+1]): binStr =  "1" + binStr
                            else:
                                for t in range(0,mlist[i]-mlist[i+1]): binStr = "0" + binStr
                                binStr =  "1" + binStr

                for t in range(0,j-2-len(binStr)): binStr = "0" + binStr      # length of BVC is j-2        
               # print("BVC code: ", binStr)
                if (verify(collatzNum, binStr)):
                    print("Correct Collatz number ", collatzNum)
                    print("BVC code: ", binStr)
            #    else: print("qj = ", qj, " Verification failed for ", collatzNum)
                        
            mlist.pop()


k = int(input("Enter the value of k, which determines the root of a subtree: "))
print("k is:", k)

j = int(input("Enter the value of the j-th stair in the tree rooted at Y_k/3: "))
print("j is:", j)

#for i in range(2,j+1)[::-1]: print(i)

#for x in range(j-1, -1, -1): print(x)
                    
                
Y_k = math.pow(2,2*k)-1
print("Y_k/3 =",Y_k/3)

if (j < 2):
    print("j is less than 2")
    sys.exit()

for qj in range(1, j):
    if (qj == 1):
        x = math.pow(2,j-1)* Y_k / 3

    #    sys.stdout.write("Traceability code for x is ") #Constructing the binary code
        binStr = ""
        for t in range(1, j-1):
            binStr = binStr + "0"
     #   sys.stdout.write("<"+binStr+">")
     #   print("")                                        # End

        if (verify(x, binStr)):
            print("Correct Collatz number ", x)
            sys.stdout.write("Binary Verification Code (BVC) for x is ")
            sys.stdout.write("<"+binStr+">")
            print("") 
            
    #    else: print("qj = ", qj, " Verification failed for ", x)

        
    if (qj == 2):
        for i in range(0, j-2):
            x = (math.pow(2,j-2)* Y_k - math.pow(2,i)*3 ) / 9
            
   #         sys.stdout.write("Traceability code for x is ") #Constructing the binary code
            binStr = ""
            for t in range(0, j-2):
                if (t == i): binStr = "1" + binStr
                else:        binStr =  "0" + binStr
    #        sys.stdout.write("<"+binStr+">")
    #        print("")                                        # End

            if (verify(x, binStr)):
                print("Correct Collatz number ", x)
                sys.stdout.write("Binary Verification Code (BVC) for x is ")
                sys.stdout.write("<"+binStr+">")
                print("")
                
       #     else: print("qj = ", qj, " Verification failed for ", x)

            
    if (qj == j-1):
         sum = 0
         for i in range(1, j-3):
             sum = sum + math.pow(3,i)
             x = (2* Y_k - sum) / math.pow(3,j-1)
             
        #     sys.stdout.write("Traceability code for x is ") #Constructing the binary code
             binStr = ""
             for t in range(1, j-1):
                 binStr = binStr + "1"
       #      sys.stdout.write("<"+binStr+">")
       #      print("")                                        # End

             if (verify(x, binStr)):
                 print("Correct Collatz number ", x)
                 sys.stdout.write("Binary Verification Code (BVC) for x is ")
                 sys.stdout.write("<"+binStr+">")
                 print("")
                 
                 
         #    else: print("qj = ", qj, " Verification failed for ", x)

        
    if (qj == j-2):
        for m in range(0, j-2):
             sum1 = 0
             sum2 = 0   
             for i in range(1, m+1):
                 sum1 = sum1 + (2 * math.pow(3,i))
             for i in range(m+1, j-2):
                 sum2 = sum2 + math.pow(3,i)
             x = (4 * Y_k - (sum1+sum2)) / math.pow(3,j-2)
             
             if (m==0):
                 binStr = ""
               #  sys.stdout.write("Traceability code for x is ") #Constructing the binary code
                 binStr = "0"
                 for t in range(1, j-2): binStr = binStr + "1"
              #   sys.stdout.write("<"+binStr+">")
              #   print("")
             else:
             #   sys.stdout.write("Traceability code for x is ") #Constructing the binary code
                binStr = ""
                for t in range(m+1, j-2): binStr = "1" + binStr
                binStr = "0" + binStr
                for t in range(1, m+1): binStr = "1" + binStr
            #    sys.stdout.write("<"+binStr+">")
           #     print("")
             if (verify(x, binStr)):
                 print("Correct Collatz number ", x)
                 sys.stdout.write("Binary Verification Code (BVC) for x is ")
                 sys.stdout.write("<"+binStr+">")
                 print("")
                 
          #   else: print("qj = ", qj, " Verification failed for ", x)

    if (2 < qj < j-2):  
        # Remaining terms when 2 < qj < j-2
        recursiveFor(qj-1, j-qj-1,qj-1, j, qj, Y_k)
        mlist.clear()
