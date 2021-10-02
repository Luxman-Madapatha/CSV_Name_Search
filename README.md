
# CSV_Name_Search
This a is an off-line Python tool for searching input names against a names database, both in CSV format, for valid names. A use case is to validate email address names against a names dictionary.

<img align="left" width="200" height="100" src="https://github.com/Luxman-Madapatha/CSV_Name_Search/blob/main/icon2.png" />
<br clear="left"/>

## Technologies

Python v3.6 or higher

## Environment
- Windows 7 or 10 Operating System
- 32 or 64 bit Architecture

## Hardware Resource Requirements

Windows 7 or Windows 10 base requirements should suffice:

https://support.microsoft.com/en-us/windows/windows-7-system-requirements-df0900f2-3513-a851-13e7-0d50bc24e15f

https://support.microsoft.com/en-us/windows/windows-10-system-requirements-6d4e9a79-66bf-7950-467c-795cf0386715

## Functional Requirements

-	Console interface [dos]
-	Input file in csv format
-	Search function from csv dictionary
-	Analytics [refer below]
-	Output to a file in csv format
-	Dictionary should be editable
-	Backup of previous OUTPUT file if available

## Analytics

- First and Last Name matching based on the dictionary
- &quot;Match rating&quot; as a percentage based on the number of characters matched

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
- The software program-script can support bulk searches [up to 1000,000 records]

## Deliverables

- Python source-code with comments

## Sample Output 

_Tool that identifies email names from the list of person dictionary names from excel  (first names and last names)_

## Data flow diagram

<img align="left" width="912" height="704" src="https://github.com/Luxman-Madapatha/CSV_Name_Search/blob/main/namesearch_data_diag2.png" />
<br clear="left"/>

## File Description

- Database.csv -> input CSV file with names which are to be validated
- firstnames and lastnames.xlsx -> the fisrt name last name XLSX dictionary file used for name validation
- namesearch.py -> the Python script to run

## How To 
Place the above three files in a directory and run the namesearch.py
[ensure all required Python libraries are installed]

 - pandas [created, manipulate and save dataframes]
- re [string regular expressions]
- time [time operations]
- csv [comma separated file]
- sys [runtime environment]
- os [operating system interface]

The name dictionary can be updated with valid names as required. and the input names can be 
relaced with a new set


## Input DATABASE.CSV file is shown below [input names to be validated]

<img align="left" width="365" height="859" src="https://github.com/Luxman-Madapatha/CSV_Name_Search/blob/main/DATABASE.PNG" />
<br clear="left"/>

## Input firstnames and lastnames.xlsx file is shown below [reference names dictionary]

<img align="left" width="348" height="901" src="https://github.com/Luxman-Madapatha/CSV_Name_Search/blob/main/firstnamesandlastnames.png" />
<br clear="left"/>


## Output CSV file is shown below

<img align="left" width="1330" height="796" src="https://github.com/Luxman-Madapatha/CSV_Name_Search/blob/main/OUTPUT1.PNG" />
<br clear="left"/>

## Support

If you are having problems, please let me know by [raising a new issue](https://github.com/Luxman-Madapatha/CSV_Name_Search/issues/new).


## License
This project is licensed with the MIT license.
