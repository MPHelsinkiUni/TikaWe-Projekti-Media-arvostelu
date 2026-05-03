# TikaWe-Projekti-Media-arvostelu
This is a repository for a web application for the University of Helsinki course - Databases and web programming. The programmer is The Dat Vo, nicknamed Michael. The application is a media review, but its structure can be generalized to other applications

# Project details
**Media review page**
- In the application, users can post reviews of any media. The review includes a title, text, media name, review number where applicable
- The user can create an account and log in to the application.
- The user can add previous posted reviews, edit them and delete them.
- The user can see the reviews added to the application and search for reviews with many options, e.g. work, reviewer, year, etc.
- The user page can show all reviews and other statistics about users.
- Reviews can be categorized by genre.
- The user can give comments to reviews and comments can link to each other.
- The average value of the work can be searched.

# Installation
- Install the flask library in your Python environment, local or otherwise.
```UNIX
$ pip install flask
```
- Create database file. This application uses database.db as its working base. Load schema.sql and schema_init.sql into it in that order. If you so choose, you may also modify schema_init.sql to include other classifications or exclude existing ones.
```UNIX
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < schema_init.sql
```
- Whenever ready, in the project folder, enter:
```UNIX
$ flask run
```
- This will enable home port 127.0.0.1:5000 where the website will be hosted locally.

# Journal
## 22.3.2026
Currently the files have merely being tested using course material. This is the first time the page will be constructed.
## 25.3.2026
In preparation for implementing the review system, the database has been massively expanded, with missing components and added redundancy. Page for adding those reviews have been prepared but function is not ready.
## 27.3.2026
The login and post system is ... "functional". The database, however, still requires referneces, indexing and other touchups. The decision was made to split up the image implementation of the database into multiple separate tables to enable easy referencing and image implementation into other components of the database.
## 29.3.2026
All base systems are functional. References have been commented out until the implementation can be "locked down". Indexing is functional. SQL injection is no longer an attack vector ... though far more simple attack vectors are possible since these reviews are identified by their id and there is no direct forbid protocol for users manually entering the edit pages of HTML links corresponding to the reviews themselves. This will have to be solved later, as well as many other UX related issues.
## 16.4.2026
After an extended break, I patched up some cybersecurity related access issues with reviews by enforcing id checks for every function sending something to the database. 
## 17.4.2026
Profile pages, classification systems have been added, with database changes and backend users.py and items.py changes to boot. In addition to this change, I have congealed as many repetitive sequences of code as possible into its own separate sections - sanity check, kill anons, kill spaghetti inputs, ghostbust and yeet empty variable. Further changes pending.
## 27.4.2026
Renamed repetitive code sections into more professional names. Enforced CSRF check on all database-interacting functions. Removed a misspelling. Removed unnecessary import lines and comments. References have been fully uncommented and usable.
## 2.5.2026
Fixed CSRF check issues. Trimmed unnecessary code and cleaned up implementation of certain seek functions. Implemented image insertions for reviews and users separately and with separate tables
## 3.5.2026
Finalised and debugged most components of the system, implemented CSS, split layout page into multiple sections, removed extraneous materials, cleaned up comments, documentation truncated and made concise. Ready for submission.

# Testing with big datasets
Upon loading in seed.py and running it normally, the app works perfectly fine and retains all base functionalities on user side, with myself having the foresight to enforce a limit on how many entries can be sent to homepage at once, though the same cannot be said of the search function, which does notably lag the page even if it is perfectly functional. This was a good wake up call to implement page settings. However, query searches and indexing seemed to have interacted in terrible and unpredictable ways and instead I proceeded to scrap it for search and implement it only for main page and comments. Otherwise everything is functional. 

An example output of browsing and insertion looked like this:
```UNIX
elapsed time: 0.01 s
127.0.0.1 - - [03/May/2026 17:41:04] "GET /login HTTP/1.1" 200 -
elapsed time: 0.01 s
127.0.0.1 - - [03/May/2026 17:41:05] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.1 s
127.0.0.1 - - [03/May/2026 17:41:09] "POST /login HTTP/1.1" 302 -
elapsed time: 0.02 s
127.0.0.1 - - [03/May/2026 17:41:10] "GET / HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:41:10] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:41:13] "GET /review_paper HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:41:13] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [03/May/2026 17:41:27] "POST /create_review HTTP/1.1" 302 -
elapsed time: 0.04 s
127.0.0.1 - - [03/May/2026 17:41:27] "GET / HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:41:27] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:41:32] "GET /search_review HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:41:32] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.03 s
127.0.0.1 - - [03/May/2026 17:41:34] "GET /search_review?query=bot HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:41:34] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.02 s
127.0.0.1 - - [03/May/2026 17:41:36] "GET /search_review?query=thread HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 17:41:36] "GET /static/main.css HTTP/1.1" 304 -
```
Even with seed.py loading a large database, no interaction lasts for longer than half a second, if even that. This database is very efficient with large numbers of users, given that the database have had indexes since the project's inception which can be verified by checking early commits. This is a very stable system.