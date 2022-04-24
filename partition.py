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
    heap = max_heap(101)
    for i in A:
        heap.push(i)
    for j in range(len(A)-1):
        largest = heap.pop()
        secondLargest = heap.pop()
        heap.push(largest - secondLargest)
    return largest - secondLargest

def repeatRandom(A, max_iter):
    l = len(A)
    # random solution S
    s = []
    sum1 = 0
    sum2 = 0
    for j in range(l):
            rand = random()
            if rand < 0.5:
                sum1 += A[j]
                s[j] = -1
            else:
                sum2 += A[j]
                s[j] = 1
    bestRes = abs(sum1-sum2)
    solution = s
    
    for i in range(max_iter):
        # generating a new potential solution
        for j in range(l):
            rand = random()
            if rand < 0.5:
                sum1 += A[j]
                s[j] = -1
            else:
                sum2 += A[j]
                s[j] = 1
        # calculate new res
        newRes = abs(sum1-sum2)

        # update best res
        if newRes < bestRes:
            bestRes = newRes
            solution = s
    return solution

def hillClimbing(A, max_iter):
    solution = []
    l = len(A)
    # generate random solution
    s = []
    sum1 = 0
    sum2 = 0
    for j in range(l):
        rand = random()
        if rand < 0.5:
            sum1 += A[j]
            s[j] = -1
        else:
            sum2 += A[j]
            s[j] = 1
    bestRes = abs(sum1-sum2)
    solution = s

    for i in range(max_iter):
        # generate a random neighbor of S (a neighbor differs from S in either one or two places)
        rand = random()
        newS = s
        if rand < 0.5:
            # differ in one place
            index = random.randint(0, l)
            newS[index] = newS[index]*-1
        else:
            #differ in two places
            index1 = random.randint(0, l)
            index2 = index1
            while index1 == index2:
                index2 = random.randint(0, l)
            newS[index1] = newS[index1]*-1
            newS[index2] = newS[index2]*-1
        # calculate new residue
        newRes = calcRes(A, newS)
        if newRes < bestRes:
            bestRes = newRes
            solution = newS
    return solution

def simulatedAnnealing():
    return 0

# prepartitioning

def prepartitioning(A, P):
    newA = []
    n = len(P)
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

def main():
    alg_code = int(sys.argv[2])
    inputfile = sys.argv[3]
    with open(inputfile) as f:
        lines = f.readlines()
    given_seq = []
    for line in lines:
        given_seq.append(int(line))
    if alg_code == 0:
        return kk(given_seq)
    elif alg_code == 1:
        return repeatRandom(given_seq, 25000)
    elif alg_code == 2:
        return hillClimbing(given_seq, 25000)
    elif alg_code == 3:
        # simulated annealing
        return 0
    elif alg_code == 11:
        # prepartitioned repeated random
        return 0
    elif alg_code == 12:
        # prepartitioned hill clmbing
        return 0
    elif alg_code == 13:
        # prepartitioned sim annealing
        return 0
