#!/bin/python3

import math
import os
import random
import re
import sys

def solution(n,k):
    print(k-1 if ((k-1) | k) <= n else k-2)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        solution(n,k)
