import sys

from .core import lookup

HELP = """
MicroDNS v0.1

Commands

lookup <hostname>

Example

python3 -m microdns google.com
"""

def main():

    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    lookup(args[0])
