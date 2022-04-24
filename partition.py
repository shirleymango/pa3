from re import I
import sys
#import numpy as np
import random
import math
from sys import getsizeof
import csv
import timeit

def T(iter):
    return (10**10) * (0.8 ** math.floor(iter/300))

def kama_karp(s):
    seq = s.copy()
    y = len(seq)-1
    for x in range(y):
        seq.sort(reverse=True)
        first = seq.pop(0)
        second = seq.pop(0)
        difference = abs(first - second)
        seq.append(difference)
    seq.sort(reverse=True)
    return abs(seq[0])

def partition_find_P(seq):
    P = []
    for i in range(len(seq)):
        P.append(random.randrange(len(seq)))
    return P 

def partition_find_A(seq,P):
    A = [0]*len(seq)
    for x in range(len(seq)):
        A[P[x]] = A[P[x]] + seq[x]
    return A
        
def randomreg(seq, iter):
    original = []
    for j in range(len(seq)):
        original.append(seq[j] if random.random() < 0.5 else -seq[j])
    smallest = abs(sum(original))
    smallestlist = original #finds list that yields smallest residue
    for i in range(iter):
        S = []
        for j in range(len(seq)):
            S.append(seq[j] if random.random() < 0.5 else -seq[j])
        comp = abs(sum(S))
        if(comp<smallest):
            smallest = comp
            smallestlist = S
    #return smallestlist, [m/n for m, n in zip(smallestlist, seq)]
    return smallest

        
def randomregpart(seq, iter):
    smallest = kama_karp(partition_find_A(seq,partition_find_P(seq)))#finds list that yields smallest residue
    for i in range(iter):
        comp = kama_karp(partition_find_A(seq,partition_find_P(seq)))
        if(comp<smallest):
            smallest = comp
    #return smallestlist, [m/n for m, n in zip(smallestlist, seq)]
    return smallest

def hillclimbing(seq, iter):
    original = []
    for j in range(len(seq)):
        original.append(seq[j] if random.random() < 0.5 else -seq[j])
    smallest = abs(sum(original))
    smallestlist = original 
    for i in range(iter):
        S = smallestlist.copy()
        randomlist = random.sample(range(0, len(seq)), 2)
        index1 = randomlist[0]
        index2 = randomlist[1]
        S[index1] = -1*smallestlist[index1]
        prob = random.random()
        if(prob < 0.5):
            S[index2] = -1*smallestlist[index2]
        comp = abs(sum(S))
        if(comp<smallest):
            smallest = comp
            smallestlist = S
    #return smallestlist, [m/n for m, n in zip(smallestlist, seq)]
    return smallest

def hillclimbingpart(seq, iter):
    P = partition_find_P(seq)
    smallestlist = partition_find_A(seq,P)
    smallest = kama_karp(smallestlist)
    for i in range(iter):
        new_P = P.copy()
        check = True
        while(check):
            rand_j = random.randrange(len(seq))
            rand_i = random.randrange(len(seq))
            if(P[rand_i]!=rand_j):
                P[rand_i]=rand_j
                check=False
        comp = kama_karp(partition_find_A(seq,new_P))
        if(comp<smallest):
            smallest = comp
            smallestlist = partition_find_A(seq,new_P)
    #return smallestlist, [m/n for m, n in zip(smallestlist, seq)]
    return smallest

def sim_annealing(seq, iter):
    original = []
    for j in range(len(seq)):
        original.append(seq[j] if random.random() < 0.5 else -seq[j])
    smallest = abs(sum(original))
    smallestlist = original 
    s_double_prime = original
    smallest_double = smallest
    for i in range(iter):
        S = smallestlist.copy()
        randomlist = random.sample(range(0, len(seq)), 2)
        index1 = randomlist[0]
        index2 = randomlist[1]
        S[index1] = -1*smallestlist[index1]
        prob = random.random()
        if(prob < 0.5):
            S[index2] = -1*smallestlist[index2]
        res = abs(sum(S))
        if(res<smallest):
            smallest = res
            smallestlist = S
        else:
            if random.random() < math.exp(-(res-smallest)/T(i)):
                smallest = res
                smallestlist = S
        if(res<smallest_double):
            smallest_double = res
            s_double_prime = S
    #return smallestlist, [m/n for m, n in zip(smallestlist, seq)]
    return smallest_double

def sim_annealing_part(seq, iter):
    P = partition_find_P(seq)
    smallestlist = partition_find_A(seq,P)
    smallest = kama_karp(smallestlist)
    s_double_prime = smallestlist
    smallest_double = smallest
    for i in range(iter):
        new_P = P.copy()
        check = True
        while(check):
            rand_j = random.randrange(len(seq))
            rand_i = random.randrange(len(seq))
            if(P[rand_i]!=rand_j):
                P[rand_i]=rand_j
                check=False
        res = kama_karp(partition_find_A(seq,new_P))
        if(res<smallest):
            smallest = res
            smallestlist = partition_find_A(seq,new_P)
        else:
            if random.random() < math.exp(-(res-smallest)/T(i)):
                smallest = res
                smallestlist = partition_find_A(seq,new_P)
        if(res<smallest_double):
            smallest_double = res
            s_double_prime = partition_find_A(seq,new_P)
    #return smallestlist, [m/n for m, n in zip(smallestlist, seq)]
    return smallest_double

def main():
    # # get arguments from command line for alg_code and input
    alg_code = int(sys.argv[2])
    input_file = sys.argv[3]
     # read in input file
    with open(input_file) as f:
        lines = f.readlines()
    given_seq = []
    for line in lines:
        given_seq.append(int(line))
    if alg_code==0:
        #given_seq = [10,8,7,6,5]
        print(kama_karp(given_seq))
        #print("hi")
    elif alg_code==1:
        #given_seq = [10,8,7,6,5]
        #print(partition(given_seq))
        print(randomreg(given_seq,25000))
        #print("hi")
    elif alg_code==2:
        print(hillclimbing(given_seq,25000))
    elif alg_code==3:
        #given_seq = [10,8,7,6,5]
        print(sim_annealing(given_seq,25000))
    elif alg_code==11:
        print(randomregpart(given_seq,25000))
    elif alg_code==12:
        #given_seq = [10,8,7,6,5]
        print(hillclimbingpart(given_seq,25000))
    elif alg_code==13:
        #given_seq = [10,8,7,6,5]
        print(sim_annealing_part(given_seq,25000))
#     elif alg_code==14:

if __name__ == "__main__":
    main()
