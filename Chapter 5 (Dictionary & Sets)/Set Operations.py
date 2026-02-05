#operations we perform to the set in mathematics are the same with set in python

S1 = {1 , 3 , 5 , 7 , 9 , 0}
S2 = {2 , 4 , 5 , 6 , 8 , 0}

print(f"UNION of two sets : {S1.union(S2)}\n")

print(f"INTERSECTION of two sets : {S1.intersection(S2)}\n")

print(f"Elements which are only in set 1 but not in set 2 : {S1.difference(S2)}\n")

print(f"Elements which are NOT COMMON in set 1 and set 1 : {S1.symmetric_difference(S2)}\n")