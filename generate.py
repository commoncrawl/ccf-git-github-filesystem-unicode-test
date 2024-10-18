from collections import defaultdict
import unicodedata
import os.path
#import re


def print_u(d):
    # get rid of the ascii, kinda... this trims too much
    #d = re.sub(r'[\w+]', '', d, flags=re.ASCII)
    print(', '.join(unicodedata.name(chr) for chr in d))


def encode(s, verbose=0):
    ret = {}
    forms = ('NFC', 'NFKC', 'NFD', 'NFKD')
    orig = set()
    for form in forms:
        ret[form] = unicodedata.normalize(form, s)
        if verbose and ret[form] == s:
            print(f'original string {s} appears to have already been in form {form}')
            orig.add(form)
    rev = defaultdict(list)
    for k, v in ret.items():
        rev[v].append(k)
        if verbose and k not in orig:
            print('in', k+': ', end='')
            print_u(v)
    for k, v in rev.items():
        if verbose and len(v) > 1:
            # expected tp happen for boring strings
            print(f'string {s} has equivalent forms {v}')
    return rev


def try_files(rev, verbose=0):
    for k, v in rev.items():
        fname = ','.join(v)+'-'+k
        if os.path.exists(fname):
            print(f'path {fname} already exists, not creating')
            continue
        with open(fname, 'w') as fd:
            pass
        if not os.path.exists(fname):
            print(f'attempting to create {fname} did not create {fname}')


verbose = 1

dangerous = ('daatsʼíin', 'dũya')

rev = encode('greg')
assert len(rev) == 1, 'greg is boring'

for d in dangerous:
    print()
    print(f'doing string {d}:')
    print_u(d)
    rev = encode(d, verbose=verbose)
    try_files(rev, verbose=verbose)
