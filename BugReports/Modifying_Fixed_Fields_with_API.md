**Title:** 
Updating fields through API that user should not be to change


**Description:**
Through API, updating an entry allows the id value to be modified. This modifies the entry on the table but also deletes its salary value.


**Steps to reproduce:**
1. In Postman, use the following:
    - URL: https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees
3. Use a GET request to get the values of an entry to modify.
4. Use a PUT request to update it. Change one of the following fields: sortKey and id, or salary.
5. By changing sortKey and id a new entry is created with a different sortKey and id.
6. By changin the salary, its value is updated on the UI.
7. By changing only the id without a salary or sortKey input on the request, the salary is set to 0.


**Expected result:**
The PUT request should not be allowed to modified values that are not meant to be edited.


**Actual result:**
A user can change the salary of an employee through API.


**Environment:**
Operating System: [Windows 11]
Browser Version: [Chrome 143.0.7499.170]
Device: [Desktop]


**Severity:** Major


**Priority:** High
