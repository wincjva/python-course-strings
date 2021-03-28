# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line

import this
import time
import math


def wait(seconds):
    time.sleep(seconds)


def my_sin(i):
    return math.sin(i)


def iso_now():
    import datetime

    return datetime.datetime.now().replace(microsecond=0).isoformat()


def platform():
    import sys

    return sys.platform


def supergreeting_wrapper(name):
    import greet

    return greet.supergreeting(name)
