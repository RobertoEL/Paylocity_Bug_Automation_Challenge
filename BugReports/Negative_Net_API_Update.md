**Title:** 
Updating id through API is allowed and deletes the salary of the employee


**Description:**
Through API, updating an entry allows the id value to be modified. This modifies the entry on the table but also deletes its salary value.


**Steps to reproduce:**
1. In Postman, use the following:
    - URL: https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees
3. Use a GET request to get the values of an entry to modify.
4. Use a PUT request to update it. Change its "id" value only.
5. Send it.
6. The entry's id is updated. This can be verified with a GET request and through the UI.


**Expected result:**
The PUT request should not be allowed to modified values that are not meant to be edited.


**Actual result:**
A user can change the id of an employee through API.

As a workaround, if the previous id value is restored, the data of the employee is recovered.


**Environment:**
Operating System: [Windows 11]
Browser Version: [Chrome 143.0.7499.170]
Device: [Desktop]


**Severity:** Minor


**Priority:** Low
