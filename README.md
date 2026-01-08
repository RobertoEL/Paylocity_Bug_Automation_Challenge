**Bug Reports**

I tested both UI and API and reported the behavior that I considered bug. Here you will be able to find some reports with descriptions and steps of how to reproduce them. I also included screenshots of the bugs.

I paid extra attention to the salary calculations and I only could find some inconsistencies during the API testing. UI seemed to be calculating the numbers correctly.

On a side note, I found some behavior that I am not sure if it would be considered a bug. Mainly because it does not break anything, it is just a weird behavior that I personally would not want in my web site, but it could be a desired functionality depending on the finished product. On this area I have to mention the sorting, the more entries there are added the harder it is to find the one you just added, because it is always sorted by id. There is no control for repeated entries additional to the unique key that every entry is assigned, which is at an extent comprehensible given the nature of human names. I found a weird behavior when I tried to add a new employee just after deleting another, but I wasn't able to replicate it again, so I could not include it here.

**Automation**

I created simple CRUD automated tests. I test the login, the adding of a new employee, the editing of an employee and the deleting of an employee.

Much can be done to improve the quality of the code liki more refactoring, the use of a page object model, or more advanced workflows, but for the time being I consider it a concise example of my skills with limited time available.

For running the tests all files should be downloaded on the same folder and then simply run the ones with filenames starting with 'Test_'.
