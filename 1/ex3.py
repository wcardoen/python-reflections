import itertools as it
import pre

a= ['a','b','c']
b= ['x','y','z']
c= [10,100]

# enumerate: returns indices and el. 
for index, item in enumerate(b):
    print(f"  El. with {index=} is {item=}")

print(f"  {20*'--'}")    

# zip: generates tuple of iterables (even of non-equal length)
#      SHORTEST  iterable is the determing factor
for item in zip(a,b,c):
    print(f"  {item=}")

print(f"  {20*'--'}")

# The itertools module has a version of zip
# which fills the 'empty spots' with None
for item in it.zip_longest(a,b,c):
    print(f"  {item=}")

print(f"  {20*'--'}")    

# zip as higher version of enumerate:
for item in zip(range(len(b)),b,c):
    print(f"  {item=}")

print(f"  {20*'--'}")

# The itertools module has a version of zip
# which fills the 'empty spots' with None
for item in it.zip_longest(a,b,c):
    print(f"  {item=}")

print(f"  {20*'--'}")    

# The itertooks module product 
# generates a Cartesian product ierable of an array of list:
s = it.product(a,b,c)
print(f"  {type(s)=}")
for item in s:
    print(f"  {item=}")    

print(f"  {20*'--'}")

# Tuple comprehension alternative 
# Do NOT use list comprehension (i.e. NOT a generator).
s= ((x,y,z) for x in a for y in b for z in c)
print(f"  {type(s)=}")
for item in s:
    print(f"  {item=}")
