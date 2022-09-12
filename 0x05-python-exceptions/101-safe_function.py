#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as err:
        print(err, file=sys.stderr)
        return None
    else:
        return fct(*args)
