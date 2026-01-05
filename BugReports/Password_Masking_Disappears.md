**Title:** 
Password masking disappears with DevTools


**Description:**
A user is able to unmask the password by using DevTools. This might enable a security breach.


**Steps to reproduce:**
1. Go to https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login
2. Right-click anywhere inside the page.
3. Click Inspect.
4. Right-click the Password field.
5. Click Inspect.
6. Inside the DevTools locate the "Type" attribute.
7. Delete its value.
8. The password is now unmasked.


**Expected result:**
A user should not be able to unmask the password field so easily.


**Actual result:**
A malicious person might be able to see the password of an authorized user.


**Environment:**
Operating System: [Windows 11]
Browser Version: [Chrome 143.0.7499.170]
Device: [Desktop]


**Severity:** Major


**Priority:** High
