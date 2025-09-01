from pathlib import Path

print(__file__)

b = Path(__file__)
print(b)

bb = Path(__file__).parent
print(bb)

bc = Path(__file__).parent.parent
print(bc)

import os

b = os.path.join(bc,"Templates")
print(b)

