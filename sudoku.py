# install the tabulate library using the pip command if not present

import numpy as np
import random
from tabulate import tabulate
import datetime
import math

#initialization
a = np.zeros((11,11), dtype = np.str_)
for i in range(11):
    for j in range(11):
        if (i+1)%4==0:
            a[i][j] = "-"
        elif (j+1)%4==0:
            a[i][j] = "|"
        else:
            a[i][j] = 0

#grid generation
start = 0
for i in range(0,11):
    num = start
    if i in (3,7):
        start -= 8
        continue
    for j in range(0,11):
        if j in (3,7):
            continue
        num += 1
        a[i][j] = num
        if num>9:
            num = 1
    start += 3

#shuffling
r1 = random.randint(0,2)
rep1 = 1
while rep1 == 1:
    r2 = random.randint(0,2)
    if r2 != r1:
        rep1 = 0
 
r3 = random.randint(4,6)
rep2 = 1
while rep2 == 1:
    r4 = random.randint(4,6)
    if r4 != r3:
        rep2 = 0

r5 = random.randint(8,10)
rep3 = 1
while rep3 == 1:
    r6 = random.randint(8,10)
    if r6 != r5:
        rep3 = 0

c1 = random.randint(0,2)
rep4 = 1
while rep4 == 1:
    c2 = random.randint(0,2)
    if c2 != c1:
        rep4 = 0
 
c3 = random.randint(4,6)
rep5 = 1
while rep5 == 1:
    c4 = random.randint(4,6)
    if c4 != c3:
        rep5 = 0

c5 = random.randint(8,10)
rep6 = 1
while rep6 == 1:
    c6 = random.randint(8,10)
    if c6 != c5:
        rep6 = 0

for i in range(0,11):
    t1 = a[r1][i]
    a[r1][i] = a[r2][i]
    a[r2][i] = t1

for i in range(0,11):
    t2 = a[r3][i]
    a[r3][i] = a[r4][i]
    a[r4][i] = t2

for i in range(0,11):
    t3 = a[r5][i]
    a[r5][i] = a[r6][i]
    a[r6][i] = t3

for i in range(0,11):
    t4 = a[i][c1]
    a[i][c1] = a[i][c2]
    a[i][c2] = t4

for i in range(0,11):
    t5 = a[i][c3]
    a[i][c3] = a[i][c4]
    a[i][c4] = t5

for i in range(0,11):
    t6 = a[i][c5]
    a[i][c5] = a[i][c6]
    a[i][c6] = t6

answer = a.copy()

#removing numbers
b = np.zeros((11,11), dtype = np.str_)

difficulty = input("Enter level of difficulty: E(easy), M(medium), D(difficult):- ")
print()
ret = 'y'
while ret == 'y':
    ret = 'n'
    if difficulty == 'E' or difficulty == 'e':
        loop = 10
    elif difficulty == 'M' or difficulty == 'm':
        loop = 14
    elif difficulty == 'D' or difficulty == 'd':
        loop = 20
    else:
        ret = 'y'
    
for mvalue in range(loop):
    rep = 1
    while rep == 1:
        n1 = random.randint(0,10)
        n2 = random.randint(0,10)
        if n1 not in (3,7) and n2 not in (3,7):
            rep = 0
        
    a[n1][n2] = " "
    for i in range(0,11):
        for j in range(0,11):
            b[j][10-i] = a[i][j]
    for i in range(0,11):
        for j in range(0,11):
            a[j][10-i] = b[i][j]
    a[n1][n2] = " "

#display puzzle
print("PUZZLE:-")
print()
print(tabulate(a))
print()

#solution logic
b = a.copy()
stime = datetime.datetime.now()
while not(np.array_equal(b, answer)):
    rret = 'true'
    while rret == 'true':
        rret = 'false'
        r = int(input("Enter row number:- "))
        if r in (1,2,3):
            r -= 1
        elif r in (4,5,6):
            r = r
        elif r in (7,8,9):
            r += 1
        else:
            print("Enter correct row number")
            rret = 'true'
            print()

    cret = 'true'
    while cret == 'true':
        cret = 'false'
        c = int(input("Enter column number:- "))
        if c in (1,2,3):
            c -= 1
        elif c in (4,5,6):
            c = c
        elif c in (7,8,9):
            c += 1
        else:
            print("Enter correct column number")
            cret = 'true'
            print()

    if a[r][c] == " ":
        dret = 'true'
        while dret == 'true':
            dret = 'false'
            digit = int(input("Enter digit to fill in the space:- "))
            if digit in (1,2,3,4,5,6,7,8,9):
                b[r][c] = digit
                print()
                print(tabulate(b))
                print()
                ltime = datetime.datetime.now()
                time = int((ltime - stime).seconds)
                minute = math.floor(time/60)
                second = time%60
                print("Time:- "+str(minute)+" minutes "+str(second)+" seconds")
                print()
            else:
                print("Enter valid digit!")
                print()
                dret = 'true'
                
    else:
        print("That position is already a part of the puzzle!")
        print()

if np.array_equal(b, answer):
    print("Congratulations! The puzzle is complete!")
