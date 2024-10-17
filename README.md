# ccf-git-github-filesystem-unicode-test

Is your life not dangerous enough? Try this on for size.

```
./generate.py

string greg appears to have been in form NFC
string greg appears to have been in form NFKC
string greg appears to have been in form NFD
string greg appears to have been in form NFKD
string greg has equivalent forms ['NFC', 'NFKC', 'NFD', 'NFKD']
string daatsʼíin appears to have been in form NFC
string daatsʼíin appears to have been in form NFKC
string daatsʼíin has equivalent forms ['NFC', 'NFKC']
string daatsʼíin has equivalent forms ['NFD', 'NFKD']
string dũya appears to have been in form NFC
string dũya appears to have been in form NFKC
string dũya has equivalent forms ['NFC', 'NFKC']
string dũya has equivalent forms ['NFD', 'NFKD']
```

Having these files, now try checking them in. Tar, untar, zip, unizp, knock
yourself out.

The one symptom know we're looking for is git sometimes mangling the
filenames. But that's just Linux; Windows and MacOS may well have some
additional symptoms.

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
string greg appears to have been in form NFC
string greg appears to have been in form NFKC
string greg appears to have been in form NFD
string greg appears to have been in form NFKD
string greg has equivalent forms ['NFC', 'NFKC', 'NFD', 'NFKD']
string daatsʼíin appears to have been in form NFC
string daatsʼíin appears to have been in form NFKC
string daatsʼíin has equivalent forms ['NFC', 'NFKC']
string daatsʼíin has equivalent forms ['NFD', 'NFKD']
path NFC,NFKC-daatsʼíin already exists, not creating
path NFD,NFKD-daatsʼíin already exists, not creating
string dũya appears to have been in form NFC
string dũya appears to have been in form NFKC
string dũya has equivalent forms ['NFC', 'NFKC']
string dũya has equivalent forms ['NFD', 'NFKD']
path NFC,NFKC-dũya already exists, not creating
path NFD,NFKD-dũya already exists, not creating
Gregs-Mac-mini:ccf-git-github-filesystem-unicode-test lindahl$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        "NFD,NFKD-daats\312\274\303\255in"
        "NFD,NFKD-d\305\251ya"

nothing added to commit but untracked files present (use "git add" to track)
```

So those 2 files exist, are untracked, and yet are not... missing.
