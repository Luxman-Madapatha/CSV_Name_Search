
# CSV_Name_Search
This a is an off-line Python tool for searching input names against a names database, both in CSV format, for valid names. 

<img align="right" width="600" height="300" src="https://github.com/Luxman-Madapatha/CSV_Name_Search/blob/main/icon2.png" />
<br clear="left"/>


## Technologies

Python v3.6 or higher

## Environment
Windows 7, or 10 Operating System 32 or 64 bit.

Python modules:

Pandas [created, manipulate and save dataframes]
re [string regular expressions]
time [time operations]
csv [comma separated file]
sys [runtime environment]
os [operating system interface] 

## Hardware Resource Requirements

Windows 7 or Windows 10 base requirements should suffice:

https://support.microsoft.com/en-us/windows/windows-7-system-requirements-df0900f2-3513-a851-13e7-0d50bc24e15f

https://support.microsoft.com/en-us/windows/windows-10-system-requirements-6d4e9a79-66bf-7950-467c-795cf0386715


## Functional Requirements

- CONSOLE INTERFACE [DOS]
- INPUT FILE IN CSV FORMAT
- SEARCH FUNCTION FROM CSV DICTIONARY
- ANALYTICS [refer below]
- OUTPUT TO A FILE IN CSV FORMAT
- **DICTIONARY SHOULD BE EDITABLE**

## Analytics

- First and Last Name matching based on the dictionary
- &quot;Match rating&quot; based on the number of characters matched

## Input / Output Format

- One input corresponding to one output record
- Output file in CSV format
- **All characters in LOWERCASE**

## Non Functional Requirements

- Coding language - Python v3
- Compatible with both Windows 7 and 10 operating systems
- The tool should be portable
- Stand-alone product
- Easy to install

## Performance Requirements

- The software program-script can be used on a low configuration PC
- The software program-script can support bulk searches [10,0000+ records]

## Deliverables

- Python source-code with comments

## Sample Output 

_Tool that identifies email names from the list of person dictionary names from excel  (first names and last names)_

### Input names

- _jroberson_
- _giovanni_
- _bob_
- _  Nathan_
- _rstellhorn_
- _watson_
- _lfoth_
- _hr_
- _jregan_
- _Paul.smith_
- _From a long list of first names_
- _Then from  last names_
- _First names or last names like Nathan or Watson can be identified easily_
- _The rest it can simply put percentage_
- _Rstellhorn_

_…………………………………………………………………………………………………………………………………………………._
- _Output should be_
- _Nathan  100% matched from first name_
- _Watson  100% matched from lastname_
- _Reganj 99% matched from lastname_
- _Jregan 99% matched from lastname_
- _Names with period, underscore, colon needs to be searched twice before and after, from first name and last name files_
- _Paul.smith (double search) 100 % matched_
- _p.smith 99% matched  _
- _smith.p_
- _paul.s_
- _note: also a place to update dictionary as and when we get new names_

- _jroberson_
- _giovanni_
- _bob_
- _Nathan_
-_rstellhorn_
- _watson_
- _lfoth_
- _hr_
- _jregan_
- _Paul.smith_
- _From a long list of first names_
- _Then from  last names_
- _First names or last names like Nathan or Watson can be identified easily_
- _The rest it can simply put percentage_
- _Rstellhorn_

_…………………………………………………………………………………………………………………………………………………._

### Output should be

- _Nathan  100% matched from first name_
- _Watson  100% matched from lastname_
- _Reganj 99% matched from lastname_
- _Jregan 99% matched from lastname_
- _Names with period, underscore, colon needs to be searched twice before and after, from first  name and last name files_
- _Paul.smith (double search) 100 % matched_
- _p.smith 99% matched_
- _smith.p_
- _paul.s_
- _note: also a place to update dictionary as and when we get new names_

........................

## Getting Started

## Support

If you are having problems, please let us know by raising a new issue.

If you are having problems, please let us know by [raising a new issue](https://github.com/Luxman-Madapatha/CSV_Name_Search/issues/new).


## License
This project is licensed with the MIT license.

