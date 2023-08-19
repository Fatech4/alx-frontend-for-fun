#!/usr/bin/python3
""" Starting a script """
if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    if args[1] != 'README.md':
        print("Missing README.md", file=sys.stderr)
        exit(1)
    else:
        exit(0)
