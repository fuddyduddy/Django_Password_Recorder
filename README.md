# Django_Password_Recorder
A password recorder built in Django Web Framework

### Preliminary design concepts:
##### Password Securities:
1. Use of module <b>Secrets</b> for password validation to strengthen password security for password cracking based on time-diff ; <br>
2. hashlib as base to convert password into SHA-256 hash object before store to database;<br>

##### DataBase:
PK: Admin ID | LastName, FirstName, Password, Email, Auth<br>
PK: Account ID | Account type, Catagory, Date Created, Date Deleted<br>
Account ID | User ID<br>
PK: UserID | User Name, Auth Level, Email, Password, Securities Questions, Token<br>
PK: Request ID | IP addresses, VisitTime, Last Visit Time<br>

##### Testing:
Pending.

WIP:<br>
2021/2/2 (12:14): Uploaded backbone for the project [django-admin startproject mydjango]<br>
2021/2/2 (12:19): Hide django secret key (my mistake and learnt from it)
2021/2/10 (18:08): Commit all changes today by VS Code.  
