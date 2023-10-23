#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fact(*args)
        return res
    except Exception as error:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
