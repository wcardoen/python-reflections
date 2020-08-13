import pre
from math import pi, cos

print(f"CHAINING COMPARISON OPERATORS::")
print(f"\nEXAMPLE 1::")
a,b,c=5,3,7
print(f"  {a<b<c=}")
# Corresponds to: (a<b) and (b<c)
#                 FALSE and TRUE => FALSE

print(f"\nEXAMPLE 2::")
print(f"  {15%4==3>2=}")
# Corresponds to: (15%4==3) and (3>2)
#             or:  TRUE     and TRUE => TRUE

print(f"\nEXAMPLE 3::")
lstA=[[1,2],["hello","world"]]
lstB=lstA
lstB[1][0]="HELLO"
lstC=lstB[:]
print(f"  {lstA is lstB is lstC=}")
print(f"  {lstA == lstB == lstC=}")
# Corresponds to: (lstA is lstB) and (lstB is lstC)
#             or: TRUE and FALSE => FALSE
# Corresponds to: (lstA == lstB) and (lstB == lstC)
#             or: TRUE and TRUE => TRUE
