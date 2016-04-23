from nose.tools import *
import random

def random_alpha(size):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(size))
