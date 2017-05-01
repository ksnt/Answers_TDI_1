#!/usr/bin/ python3
# -*- coding: UTF-8 -*-
# Author: Takayuki Kaisen
#

import numpy as np

def fact(n):
    if(n==0): 1
    else: n * fact(n-1)
    
def main(n):
    nums = set([i for i in range(1,n+1)])
    #tmp1 = 0
    #tmp2 = 0
    result = []
    for n1 in nums:
        seq = []
        used_nums= set()
        tmp1 = 0
        tmp2 = 0
        tmp1  += n1
        used_nums = set([tmp1])
        seq.append(n1)
        #nums.remove(n1)
        #print(n1)
        for n2 in nums.difference(used_nums):
            tmp2 += n2
            #nums.remove(n2)
            used_nums.add(n2)
            seq.append(np.abs(tmp2 - tmp1))
            tmp1 = 0
            #print(n2)
            for n3 in nums.difference(used_nums):
                tmp1 += n3
                #nums.remove(n3)
                used_nums.add(n3)
                seq.append(np.abs(tmp1 - tmp2))
                tmp2 = 0
                #print(n3)
                for n4 in nums.difference(used_nums):
                    tmp2 += n4
                    #nums.remove(n4)
                    used_nums.add(n4)
                    seq.append(np.abs(tmp2 - tmp1))
                    tmp1 = 0
                    for n5 in nums.difference(used_nums):
                        tmp1 += n5
                        #nums.remove(n5)
                        used_nums.add(n5)
                        seq.append(np.abs(tmp1 - tmp2))
                        tmp2 = 0
                        for n6 in nums.difference(used_nums):
                            tmp2 += n6
                            #nums.remove(n6)
                            used_nums.add(n6)
                            seq.append(np.abs(tmp2 - tmp1))
                            tmp1 = 0
                            for n7 in nums.difference(used_nums):
                                tmp1 += n7
                                #nums.remove(n7)
                                used_nums.add(n7)
                                seq.append(np.abs(tmp1 - tmp2))
                                tmp2 = 0
                                for n8 in nums.difference(used_nums):
                                    tmp2 += n8
                                    #nums.remove()
                                    used_nums.add(n8)
                                    seq.append(np.abs(tmp2 - tmp1))
                                    tmp1 = 0
                                    for n9 in nums.difference(used_nums):
                                       tmp1 += n9
                                       used_nums.add(n9)
                                       seq.append(np.abs(tmp1 - tmp2))
                                       tmp2 = 0
                                       for n10 in nums.difference(used_nums):
                                           tmp2 += n10
                                           used_nums.add(n10)
                                           seq.append(np.abs(tmp2 - tmp1))
                                           tmp1 = 0
                                           result.append(sum(seq))
                                           #print(used_nums)
                                           #print(seq)
    print(np.mean(result))


if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 2:
        n = args[1]
    else:
        print("The number of given arguments is wrong. \nYou should give only one argument.\n")
        sys.exit()
    main(int(n))