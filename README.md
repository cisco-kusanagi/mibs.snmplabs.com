# mibs.snmplabs.com

Scrape of all MIBs taken from http://mibs.snmplabs.com/asn1/, as of 04/29/2019.

Created with a recursive wget command.

This repo only exists because those sources don't seem to be in github.

All original MIB files are in the 'asn1' directory.

All compiled MIB .py files are in the 'pysnmp' directory.

# Instructions

```
# Create the Python enviroment
pipenv shell
pipenv install

# Fetching all mibs
make fetch

# Comiling all mibs
make compile
```
