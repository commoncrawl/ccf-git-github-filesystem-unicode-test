# ccf-git-github-filesystem-unicode-test

Is your life not dangerous enough? Try this on for size.

```
python ./generate.py

doing string daatsʼíin:
LATIN SMALL LETTER D, LATIN SMALL LETTER A, LATIN SMALL LETTER A, LATIN SMALL LETTER T, LATIN SMALL LETTER S, MODIFIER LETTER APOSTROPHE, LATIN SMALL LETTER I WITH ACUTE, LATIN SMALL LETTER I, LATIN SMALL LETTER N
original string daatsʼíin appears to have already been in form NFC
original string daatsʼíin appears to have already been in form NFKC
in NFD: LATIN SMALL LETTER D, LATIN SMALL LETTER A, LATIN SMALL LETTER A, LATIN SMALL LETTER T, LATIN SMALL LETTER S, MODIFIER LETTER APOSTROPHE, LATIN SMALL LETTER I, COMBINING ACUTE ACCENT, LATIN SMALL LETTER I, LATIN SMALL LETTER N
in NFKD: LATIN SMALL LETTER D, LATIN SMALL LETTER A, LATIN SMALL LETTER A, LATIN SMALL LETTER T, LATIN SMALL LETTER S, MODIFIER LETTER APOSTROPHE, LATIN SMALL LETTER I, COMBINING ACUTE ACCENT, LATIN SMALL LETTER I, LATIN SMALL LETTER N
string daatsʼíin has equivalent forms ['NFC', 'NFKC']
string daatsʼíin has equivalent forms ['NFD', 'NFKD']
path NFC,NFKC-daatsʼíin already exists, not creating
path NFD,NFKD-daatsʼíin already exists, not creating

doing string dũya:
LATIN SMALL LETTER D, LATIN SMALL LETTER U WITH TILDE, LATIN SMALL LETTER Y, LATIN SMALL LETTER A
original string dũya appears to have already been in form NFC
original string dũya appears to have already been in form NFKC
in NFD: LATIN SMALL LETTER D, LATIN SMALL LETTER U, COMBINING TILDE, LATIN SMALL LETTER Y, LATIN SMALL LETTER A
in NFKD: LATIN SMALL LETTER D, LATIN SMALL LETTER U, COMBINING TILDE, LATIN SMALL LETTER Y, LATIN SMALL LETTER A
string dũya has equivalent forms ['NFC', 'NFKC']
string dũya has equivalent forms ['NFD', 'NFKD']
path NFC,NFKC-dũya already exists, not creating
path NFD,NFKD-dũya already exists, not creating
```

Having these files, now try checking them in. Tar, untar, zip, unizp, knock
yourself out.

We're looking for different behavior in different situations. Linux is usually
clean, however, sometimes it can have problems.

## MacOS

after git checkout:

```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        "NFD,NFKD-daats\312\274\303\255in"
        "NFD,NFKD-d\305\251ya"
```

And then

```
$ python3 generate.py

doing string daatsʼíin:
LATIN SMALL LETTER D, LATIN SMALL LETTER A, LATIN SMALL LETTER A, LATIN SMALL LETTER T, LATIN SMALL LETTER S, MODIFIER LETTER APOSTROPHE, LATIN SMALL LETTER I WITH ACUTE, LATIN SMALL LETTER I, LATIN SMALL LETTER N
original string daatsʼíin appears to have been in form NFC
original string daatsʼíin appears to have been in form NFKC
in NFD: LATIN SMALL LETTER D, LATIN SMALL LETTER A, LATIN SMALL LETTER A, LATIN SMALL LETTER T, LATIN SMALL LETTER S, MODIFIER LETTER APOSTROPHE, LATIN SMALL LETTER I, COMBINING ACUTE ACCENT, LATIN SMALL LETTER I, LATIN SMALL LETTER N
in NFKD: LATIN SMALL LETTER D, LATIN SMALL LETTER A, LATIN SMALL LETTER A, LATIN SMALL LETTER T, LATIN SMALL LETTER S, MODIFIER LETTER APOSTROPHE, LATIN SMALL LETTER I, COMBINING ACUTE ACCENT, LATIN SMALL LETTER I, LATIN SMALL LETTER N
string daatsʼíin has equivalent forms ['NFC', 'NFKC']
string daatsʼíin has equivalent forms ['NFD', 'NFKD']
path NFC,NFKC-daatsʼíin already exists, not creating
path NFD,NFKD-daatsʼíin already exists, not creating

doing string dũya:
LATIN SMALL LETTER D, LATIN SMALL LETTER U WITH TILDE, LATIN SMALL LETTER Y, LATIN SMALL LETTER A
string dũya appears to have been in form NFC
string dũya appears to have been in form NFKC
in NFD: LATIN SMALL LETTER D, LATIN SMALL LETTER U, COMBINING TILDE, LATIN SMALL LETTER Y, LATIN SMALL LETTER A
in NFKD: LATIN SMALL LETTER D, LATIN SMALL LETTER U, COMBINING TILDE, LATIN SMALL LETTER Y, LATIN SMALL LETTER A
string dũya has equivalent forms ['NFC', 'NFKC']
string dũya has equivalent forms ['NFD', 'NFKD']
path NFC,NFKC-dũya already exists, not creating
path NFD,NFKD-dũya already exists, not creating

$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        "NFD,NFKD-daats\312\274\303\255in"
        "NFD,NFKD-d\305\251ya"

nothing added to commit but untracked files present (use "git add" to track)
```

So those 2 files exist, are untracked, and yet are not... missing.
