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
