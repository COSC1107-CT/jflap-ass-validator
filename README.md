# RMIT CSIT CT Assignment Format Checker

## Background

During previous years, many students submitted incorrectly formatted zip files for their first [JFLAP-based](http://www.jflap.org/) assignment resulting in no marks or penalties. 

As a way to mitigate this problem, this script intents to perform some checks for the formatting of the zip files prior to submission to ensure the following:

1. The zip file exists and is indeed a zip compressed file.
2. The zip file is named corrected (7 digit number followed by .zip)
3. The zip file contains all of the expected files including bonus questions files. 
4. The zip file does not contain unexpected files and folders, including accidentally nesting the submission files too deeply.

This validator _only checks at the file names_ and locations in the zip file, but _does no check on the validity of each file beyond their names_. For example, it does not check file encodings (use `file` for that) or that the content in each file  (e.g., whether it is JFLAP XML data or text data).

## Prerequisites

1. Python Version 2 or 3, with standard packages: `os`, `sys`, `re`, `zipfile`, and `argparse`.
2. Windows, linux or MacOS environment.


## Running the script

This script is intended for students to download and run locally. 

```
$ python validator.py <fullpath_to_zipfile>.zip
```

For help, use `-h` option:

```
[ssardina@Thinkpad-X1 jflap-ass-validator.git]$ python validator.py -h
usage: validator.py [-h] domain-problem

Validate file content in zip submission file for COSC1107/1105 Assignment 1.
Will check if it is a zip file and if the name of the files inside are
correct.Note it does NOT check the encoding of the files or their types (text
or JFLAP).

positional arguments:
  domain-problem  .zip file containing the submission

optional arguments:
  -h, --help      show this help message and exit
```


### Example of running against a correct file:
```
$python validator.py samples/correct/3530000.zip 

OK: ZIP file name: 3530000.zip is ok.
OK: File: E1-Qa1.txt is named correctly
OK: File: E1-Qa2.txt is named correctly
OK: File: E1-Qa3.txt is named correctly
OK: File: E1-Qa4.txt is named correctly
OK: File: E1-Qa5.txt is named correctly
OK: File: E1-Qa6.txt is named correctly
OK: File: E1-Qa7.txt is named correctly
OK: File: E1-Qb1.txt is named correctly
OK: File: E1-Qb2.txt is named correctly
OK: File: E1-Qb3.txt is named correctly
OK: File: E1-Qb4.txt is named correctly
OK: File: E2-Qa1.txt is named correctly
OK: File: E2-Qa2.txt is named correctly
OK: File: E2-Qa3.txt is named correctly
OK: File: E2-Qa4.txt is named correctly
OK: File: E2-Qb1.txt is named correctly
OK: File: E2-Qc1.txt is named correctly
OK: File: E2-Qc2.txt is named correctly
OK: File: E3-Qa1.txt is named correctly
OK: File: E3-Qa2.txt is named correctly
OK: File: E3-Qa3.txt is named correctly
OK: File: E3-Qa4.jff is named correctly
OK: File: E3-Qa5.jff is named correctly
OK: File: E3-Qb1.jff is named correctly
OK: File: E3-Qb2.txt is named correctly
OK: File: E3-Qc1.txt is named correctly
OK: File: E3-Qc2.txt is named correctly
OK: File: E4-Qa1.jff is named correctly
OK: File: E4-Qb1.jff is named correctly
OK: File: E5-Qb.txt is named correctly
All tests successful, your zip file is correctly formatted.

```

### Example of a zip file missing exercise 1 files:

```
$python validator.py samples/missing_e1/3530000.zip 
OK: ZIP file name: 3530000.zip is ok.
FAIL: File: E1-Qa1.txt is not found in the zip root.
FAIL: File: E1-Qa2.txt is not found in the zip root.
FAIL: File: E1-Qa3.txt is not found in the zip root.
FAIL: File: E1-Qa4.txt is not found in the zip root.
FAIL: File: E1-Qa5.txt is not found in the zip root.
FAIL: File: E1-Qa6.txt is not found in the zip root.
FAIL: File: E1-Qa7.txt is not found in the zip root.
FAIL: File: E1-Qb1.txt is not found in the zip root.
FAIL: File: E1-Qb2.txt is not found in the zip root.
FAIL: File: E1-Qb3.txt is not found in the zip root.
FAIL: File: E1-Qb4.txt is not found in the zip root.
OK: File: E2-Qa1.txt is named correctly
OK: File: E2-Qa2.txt is named correctly
OK: File: E2-Qa3.txt is named correctly
OK: File: E2-Qa4.txt is named correctly
OK: File: E2-Qb1.txt is named correctly
OK: File: E2-Qc1.txt is named correctly
OK: File: E2-Qc2.txt is named correctly
OK: File: E3-Qa1.txt is named correctly
OK: File: E3-Qa2.txt is named correctly
OK: File: E3-Qa3.txt is named correctly
OK: File: E3-Qa4.jff is named correctly
OK: File: E3-Qa5.jff is named correctly
OK: File: E3-Qb1.jff is named correctly
OK: File: E3-Qb2.txt is named correctly
OK: File: E3-Qc1.txt is named correctly
OK: File: E3-Qc2.txt is named correctly
OK: File: E4-Qa1.jff is named correctly
OK: File: E4-Qb1.jff is named correctly
OK: File: E5-Qb.txt is named correctly
One or more tests failed. Please check the results above for details.

```

### Example where the zip file has got extra nesting:

```
$python validator.py samples/incorrect_nesting/3530000.zip 

OK: ZIP file name: 3530000.zip is ok.
FAIL: File: E1-Qa1.txt is not found in the zip root.
FAIL: File: E1-Qa2.txt is not found in the zip root.
FAIL: File: E1-Qa3.txt is not found in the zip root.
FAIL: File: E1-Qa4.txt is not found in the zip root.
FAIL: File: E1-Qa5.txt is not found in the zip root.
FAIL: File: E1-Qa6.txt is not found in the zip root.
FAIL: File: E1-Qa7.txt is not found in the zip root.
FAIL: File: E1-Qb1.txt is not found in the zip root.
FAIL: File: E1-Qb2.txt is not found in the zip root.
FAIL: File: E1-Qb3.txt is not found in the zip root.
FAIL: File: E1-Qb4.txt is not found in the zip root.
FAIL: File: E2-Qa1.txt is not found in the zip root.
FAIL: File: E2-Qa2.txt is not found in the zip root.
FAIL: File: E2-Qa3.txt is not found in the zip root.
FAIL: File: E2-Qa4.txt is not found in the zip root.
FAIL: File: E2-Qb1.txt is not found in the zip root.
FAIL: File: E2-Qc1.txt is not found in the zip root.
FAIL: File: E2-Qc2.txt is not found in the zip root.
FAIL: File: E3-Qa1.txt is not found in the zip root.
FAIL: File: E3-Qa2.txt is not found in the zip root.
FAIL: File: E3-Qa3.txt is not found in the zip root.
FAIL: File: E3-Qa4.jff is not found in the zip root.
FAIL: File: E3-Qa5.jff is not found in the zip root.
FAIL: File: E3-Qb1.jff is not found in the zip root.
FAIL: File: E3-Qb2.txt is not found in the zip root.
FAIL: File: E3-Qc1.txt is not found in the zip root.
FAIL: File: E3-Qc2.txt is not found in the zip root.
FAIL: File: E4-Qa1.jff is not found in the zip root.
FAIL: File: E4-Qb1.jff is not found in the zip root.
FAIL: File: E5-Qb.txt is not found in the zip root.
FAIL: File: 3530000/ is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qa4.jff is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E2-Qa2.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E5-Qb.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E2-Qa3.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qa5.jff is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E2-Qa1.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qa1.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E2-Qa4.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qa2.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qa3.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qa1.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qa2.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qa3.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E4-Qb1.jff is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qa7.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qa6.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qa4.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qa5.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qb4.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qb2.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qb3.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E4-Qa1.jff is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E1-Qb1.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qb1.jff is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qb2.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E2-Qc2.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E2-Qc1.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E2-Qb1.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qc1.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
FAIL: File: 3530000/E3-Qc2.txt is in the zip but it's not expected. Please ensure the file is in the zip root.
One or more tests failed. Please check the results above for details.

$

```

