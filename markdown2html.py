#!/usr/bin/python3
""" Starting a script """
if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    if not (args[1].endswith("md")):
        print("Missing {}".format(args[1].replace(".html", ".md")),
              file=sys.stderr)
        exit(1)
    else:
        exit(0)
