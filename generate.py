from collections import defaultdict
import unicodedata
import os.path


def encode(s, verbose=0):
    ret = {}
    forms = ('NFC', 'NFKC', 'NFD', 'NFKD')
    for form in forms:
        ret[form] = unicodedata.normalize(form, s)
        if verbose and ret[form] == s:
            print(f'string {s} appears to have been in form {form}')
    rev = defaultdict(list)
    for k, v in ret.items():
        rev[v].append(k)
    for k, v in rev.items():
        if len(v) > 1:
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

rev = encode('greg', verbose=verbose)
assert len(rev) == 1, 'greg is boring'

for d in dangerous:
    rev = encode(d, verbose=verbose)
    try_files(rev, verbose=verbose)
