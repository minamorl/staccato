import operator
import itertools


def chunk(it, n):
    op = operator.itemgetter(1)
    for key, subitr in itertools.groupby(enumerate(it), lambda x: x[0] // n):
        yield map(op, subitr)
