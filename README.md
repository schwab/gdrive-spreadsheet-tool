# gdrive-spreadsheet-tool
##Project Description
1. input: A folder containing google spreadsheet files, with a list of company information and email addresses.

2. Functions: 
Find and count all email addresses. Find and count all rows with no email addresses. Find duplicate files and delete the older one. Find duplicate emails and delete the older entry (both in the same file or in different files within the folder).
Find and highlight rows containing emails with a typo, for example Example@examplecom (missing .) or example at example.com (missing @))

3. Output: 
** All the files in the folder with corrected data.
** A "map" file containing a list of all the files in the folder and information about the files in the folder:
    ** A. Total number of emails per file and in all folder
    ** B. Total number of rows per file and in all folder
