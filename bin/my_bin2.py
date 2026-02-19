#!/usr/bin/env -S uv run python
from src.my_lib2 import multiply
import sys

print(multiply(int(sys.argv[1]), int(sys.argv[2])))
