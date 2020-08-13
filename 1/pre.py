#!/usr/bin/env python

import sys
major=int(sys.version_info[0])
minor=int(sys.version_info[1])

if major!= 3 or minor<8:
    STR_ERR=f"  Python>=3.8 REQUIRED but running {major}.{minor}!"
    sys.exit(STR_ERR)

