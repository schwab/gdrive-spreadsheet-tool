# gdrive-spreadsheet-tool
##Project Description
### Input
---
A folder containing google spreadsheet files, with a list of company information and email addresses.

### Functions
---
1. Find and count all email addresses. 
2. Find and count all rows with no email addresses. 
3. Find duplicate files and delete the older one. 
4. Find duplicate emails and delete the older entry (both in the same file or in different files within the folder).
5. Find and highlight rows containing emails with a typo, for example Example@examplecom (missing .) or example at example.com (missing @))

### Output
---
1. All the files in the folder with corrected data.
2.  A "map" file containing a list of all the files in the folder and information about the files in the folder:
    * Total number of emails per file and in all folder
    * Total number of rows per file and in all folder
