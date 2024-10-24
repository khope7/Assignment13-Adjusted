#Task 1: Email Extraction Enhancement
# 
# Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). Modify the script to extract all email addresses except those from the specified domain.
#
#Code Example:
#
#import re
#
#text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
#emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
#print(emails)

#Writing code for PythonRegExpressionsDeepDiveTask1


#Instantiating Regular Expressions
import re

#Instantiating example text
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

#Instantiating example regex and adjusting for exclude method
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
                    
#Creating Welcome message
print("Printing all domains that exclude 'exclude.com':")

#Using for loop for print format
for email in emails:
    print(email)