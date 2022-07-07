#!/usr/bin/env python3

# Traditional if/elif/else statements
def find_capital(country):
    if country == 'France':
        return 'Paris'
    elif country == 'Germany':
        return 'Berlin'
    elif country == 'Netherlands':
        return 'Amsterdam'
    elif country == 'Belgium':
        return 'Brussels'
    else:
        return 'SORRY!'

for country in ['Belgium', 'Poland']:
    print(f"  Country:{country:>15s} -> Capital:{find_capital(country):>10s}")
print(f"\n\n")


# Match: correspondence 
def find_capital2(country):
    match country:
        case 'France':
             return 'Paris'
        case 'Germany':
             return 'Berlin'
        case 'Netherlands':
             return 'Amsterdam'
        case 'Belgium':
             return 'Brussels'
        case _:
             return 'Sorry!'
    
for country in ['Belgium', 'Denmark']:
    print(f"  Country:{country:>15s} -> Capital:{find_capital2(country):>10s}")
print(f"\n\n")


# Match: combinations of patterns 
def find_continent(country):
    match country:
        case 'Belgium'|'France'|'Germany'|'Netherlands':
            return 'Europe'
        case 'China'|'India'|'Japan':
            return 'Asia'
        case _:
            return 'Sorry!'
for country in ['France','China','USA','India']:
    print(f"  Country:{country:>15s} -> Continent:{find_continent(country):>10s}") 
print(f"\n\n")

# Unpacking:
def find_location(point):
    match point:
        case (0,0,0):
            return "Origin"
        case (x,0,0):
            return "Pt. on x-axis"
        case (0,y,0):
            return "Pt. on y-axis"
        case (0,0,z):
            return "Pt. on z-axis"
        case (x,y,0):
            return "Pt. in the xy-plane"
        case (x,0,z):
            return "Pt. in the xz-plane"
        case (0,y,z):
            return "Pt. in the yz-plane"
        case (x,y,z):
            return "Reg. pt."
        case _:
            return "NOT a 3D-point"
for item in [(3,4,5), [2,0,0], (0,0,0), (0,3,2), (3,4,5,6)]:
    print(f"  Pt.:{str(item):>15s}   Type:{find_location(item)}")
print(f"\n\n")


