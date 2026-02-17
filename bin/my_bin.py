#!/usr/bin/env -S uv run python
from my_lib import add
import sys

print(add(int(sys.argv[1]), int(sys.argv[2])))
