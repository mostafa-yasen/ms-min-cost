from typing import List

def solution(S: str, C: List[int]):
    S = [c for c in S]
    b = [""]
    total = 0
    dublicates = [[0]]

    for i, c in enumerate(S):
        if c == b[-1]:
            dublicates[-1].append(C[i])
        else:
            dublicates.append([C[i]])
        
        b.append(c)

    for l in dublicates:
        while len(l) > 1:
            cost = min(l)
            total += cost
            l.remove(cost)

    return total

r = solution("aaabbbccc", [5,3,1,7,2,8,5,8,7])
print(r)

