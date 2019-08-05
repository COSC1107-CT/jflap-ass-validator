# RMIT CSIT CT Assignment Format Checker

## Background
During previous years, many students submitted incorrectly formatted zip documents for 
their first assignment resulting in as 0 grade. As a way to mitigate this problem, this
script intents to check the formatting of the zip files prior to submission to ensure the following:
1. The zip file is named corrected (7 digit number followed by .zip)
2. The zip file contains all of the expected files including bonus questions files. 
3. The zip file does not contain unexpected files and folders. 
   Including accidentally nesting the submission files too deeply.

## Prerequisites
1. Python Version 2 or 3.
2. Windows, linux or MacOS environment.

## Running the script
This script is intended for students to download and run locally. 
```
$python validator.py <fullpath_to_zipfile>.zip
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

