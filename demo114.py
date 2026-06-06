'''
create list of cndidates
add candidtes from last
remove one by one candidates from first
add a cndidate inbetween at highest priority

'''
from collections import deque
candidates = deque(["arshu", "kallu", "sandy"])

print("Initial candidates:", list(candidates))

candidates.append("rolex")
candidates.append("prams")

print("After adding at last:", list(candidates))

candidates.appendleft("subhani")

print("After adding highest priority candidate:", list(candidates))


while candidates:
    removed = candidates.popleft()
    print("Removed:", removed)
    print("Remaining candidates:", list(candidates))