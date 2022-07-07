#!/bin/bash

capitals1 = {'france':'paris', 'germany':'berlin','netherlands':'amsterdam'}
capitals2 = {'france':'paris', 'belgium':'brussels', 'denmark':'copenhagen'}

# Merging: Creation of a new dict object
capitals3 = capitals1 | capitals2
print(f"  capitals3:\n{capitals3}")

# Update in-place operation
capitals1 |= capitals2
print(f"  capitals1:\n{capitals1}")
