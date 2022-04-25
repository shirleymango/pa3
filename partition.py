import math
import random
from re import L
import sys

# helper function
def calcRes(A, s):
    l = len(A)
    res = 0
    for i in range(l):
        res += A[i]*s[i]
    return res

def kk(A):
    seq = A.copy()
    l = len(seq)-1
    for x in range(l):
        seq.sort(reverse=True)
        first = seq.pop(0)
        second = seq.pop(0)
        difference = abs(first - second)
        seq.append(difference)
    seq.sort(reverse=True)
    return abs(seq[0])

def repeatRandom(A, max_iter):
    # random solution S
    S = []
    for j in range(len(A)):
        S.append(A[j] if random.random() < 0.5 else -A[j])
    residue = abs(sum(S))
    for i in range(max_iter):
        # generating a new potential solution
        newS = []
        for j in range(len(A)):
            newS.append(A[j] if random.random() < 0.5 else -A[j])
        newRes = abs(sum(newS))
        if(newRes<residue):
            residue = newRes
    #return smallestlist, [m/n for m, n in zip(smallestlist, seq)]
    return residue

def repeatRandomPart(A, max_iter):
    # random solution S
    S = []
    for j in range(len(A)):
        S.append(A[j] if random.random() < 0.5 else -A[j])
    residue = abs(sum(S))
    for i in range(max_iter):
        # generating a new potential solution
        newS = []
        for j in range(len(A)):
            newS.append(A[j] if random.random() < 0.5 else -A[j])
        newRes = abs(sum(newS))
        if(newRes<residue):
            residue = newRes
    #return smallestlist, [m/n for m, n in zip(smallestlist, seq)]
    return residue

def hillClimbing(A, max_iter):
    S = []
    for j in range(len(A)):
        S.append(A[j] if random.random() < 0.5 else -A[j])
    residue = abs(sum(S))
    for i in range(max_iter):
        newS = S.copy()
        randomlist = random.sample(range(0, len(A)), 2)
        index1 = randomlist[0]
        index2 = randomlist[1]
        newS[index1] = -1*S[index1]
        prob = random.random()
        if(prob < 0.5):
            newS[index2] = -1*S[index2]
        newRes = abs(sum(newS))
        if(newRes<residue):
            residue = newRes
    return residue

def simulatedAnnealing(A, max_iter):
    # random solution S
    S = []
    for j in range(len(A)):
        S.append(A[j] if random.random() < 0.5 else -A[j])
    smallest = abs(sum(S))
    smallestlist = S 
    smallest_double = smallest
    for i in range(max_iter):
        # neighbor S
        neighborS = smallestlist.copy()
        randomlist = random.sample(range(0, len(A)), 2)
        index1 = randomlist[0]
        index2 = randomlist[1]
        neighborS[index1] = -1*smallestlist[index1]
        prob = random.random()
        if(prob < 0.5):
            neighborS[index2] = -1*smallestlist[index2]
        res = abs(sum(neighborS))
        if(res<smallest):
            smallest = res
            smallestlist = neighborS
        else:
            if random.random() < math.exp(-(res-smallest)/T(i)):
                smallest = res
                smallestlist = neighborS
        if(res<smallest_double):
            smallest_double = res
    return smallest_double

# prepartitioning
def prepartitioning(A):
    # generating P
    n = len(A)
    P = []
    for i in range(n):
        P.append(random.randrange(n))
    
    # generating A
    newA = [0]*n
    for j in range(n):
        newA[P[j]] = newA[P[j]] + A[j]
    return newA

    # MAX HEAP DATA STRUCTURE
    # defining a class max_heap for the heap data structure
class max_heap: 
    def __init__(self, sizelimit):
        self.sizelimit = sizelimit
        self.cur_size = 0
        self.Heap = [0]*(self.sizelimit + 1)
        self.Heap[0] = sys.maxsize
        self.root = 1
 
 
    def swapnodes(self, node1, node2):
        self.Heap[node1], self.Heap[node2] = self.Heap[node2], self.Heap[node1]
  
    # THE MAX_HEAPIFY FUNCTION
    def max_heapify(self, i):
  
        # If the node is a not a leaf node and is lesser than any of its child
        if not (i >= (self.cur_size//2) and i <= self.cur_size):
            if (self.Heap[i] < self.Heap[2 * i]  or  self.Heap[i] < self.Heap[(2 * i) + 1]): 
                if self.Heap[2 * i] > self.Heap[(2 * i) + 1]:
     # Swap the node with the left child and call the max_heapify function on it
                    self.swapnodes(i, 2 * i)
                    self.max_heapify(2 * i)
  
                else:
                # Swap the node with right child and then call the max_heapify function on it
                    self.swapnodes(i, (2 * i) + 1)
                    self.max_heapify((2 * i) + 1)
  
 
 
    # push function
    def push(self, element):
        if self.cur_size >= self.sizelimit :
            return
        self.cur_size+= 1
        self.Heap[self.cur_size] = element 
        current = self.cur_size
        while self.Heap[current] > self.Heap[current//2]:
            self.swapnodes(current, current//2)
            current = current//2
  
  
    # pop function
    def pop(self):
        last = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.cur_size]
        self.cur_size -= 1
        self.max_heapify(self.root)
        return last
  
  
    # build function
    def build(self): 
        for i in range(self.cur_size//2, 0, -1):
            self.max_heapify(i)

def T(iter):
    return (10**10) * (0.8 ** math.floor(iter/300))

def main():
    alg_code = int(sys.argv[2])
    inputfile = sys.argv[3]
    with open(inputfile) as f:
        lines = f.readlines()
    given_seq = []
    for line in lines:
        given_seq.append(int(line))
    if alg_code == 0:
        print(kk(given_seq))
    elif alg_code == 1:
        print(repeatRandom(given_seq, 25000))
    elif alg_code == 2:
        print(hillClimbing(given_seq, 25000))
    elif alg_code == 3:
        # simulated annealing
        print(simulatedAnnealing(given_seq, 25000))
    elif alg_code == 11:
        # prepartitioned repeated random
        print(repeatRandom(prepartitioning(given_seq), 25000))
    elif alg_code == 12:
        # prepartitioned hill clmbing
        print(hillClimbing(prepartitioning(given_seq), 25000))
    elif alg_code == 13:
        # prepartitioned sim annealing
        print(0)

if __name__ == "__main__":
    main()
