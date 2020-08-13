import pre
from math import pi, cos

print(f"F-strings::")
print(f"EXAMPLE 1::")
artist={"von Beethoven":"Bonn",
        "de Balzac":"Tours",
        "van Eyck":"Maaseik",
        "Alighieri":"Firenze"}

# Python >=2.7 approach
for person in artist.keys():
    print("{0:>13} was born in {1}".format(person,artist[person]))

# Python >=3.6 approach (iter #1)
for person in artist.keys():
    print(f"{person:>13} was born in {artist[person]}")

# Python >=3.6 approach (iter #2)
WIDTH = max(( len(item) for item in artist.keys()))
for person in artist.keys():
    print(f"{person:>{WIDTH}} was born in {artist[person]}")


print(f"\nEXAMPLE 2::")
WIDTH=15
PRECISION=10
print(f"Value of pi ='{pi:{WIDTH}.{PRECISION}}'")

# Self-documenting/Debugging:
print(f"\nEXAMPLE 3::")
WIDTH=10
PRECISION=4
print(f"{cos(pi/4.0)=}")
print(f"{cos(pi/4.0)=:{WIDTH}.{PRECISION}}")
