**Title:** 
Dependents field in Add Employee window allows special characters, but truncates result.


**Description:**
A user is able to enter any amount and kind of characters in the Dependents field in the Add Employee window and click Add as long as the first two characters is a number between 0 and 32. The entry is added but the Dependents field is truncated using only the first start of the entered value if it matches the Dependents field's criteria.


**Steps to reproduce:**
1. Go to https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login
2. Login.
3. Click the Add Employee button.
4. Enter aa name in First Name.
5. Enter a last name in Last Name.
6. Enter a number between 0 and 32 in the Dependents field.
7. Add a string of any characters and any length that starts with a special character to the value in Dependents field.
8. Click Add.
9. The entry is added to the table and the value of the Dependents field is the first number entered, before the special characters.


**Expected result:**
The Add Employee window should not let the user enter characters that are not numbers in the Dependents field.


**Actual result:**
The user is able to save entries to the Employees table as long as the Dependents field's value starts with a number between 0 and 32 followed by a special character and a string of any characters.


**Environment:**
Operating System: [Windows 11]
Browser Version: [Chrome 143.0.7499.170]
Device: [Desktop]


**Severity:** Minor


**Priority:** Low
