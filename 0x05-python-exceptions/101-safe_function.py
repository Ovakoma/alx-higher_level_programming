#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    else:
        return result
