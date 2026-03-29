# TikaWe-Projekti-Media-arvostelu
This is a repository for a web application for the University of Helsinki course - Databases and web programming. The programmer is The Dat Vo, nicknamed Michael. The application is a media review, but its structure can be generalized to other applications

# Project details
**Media review page**
- In the application, users can post reviews of any media. The review includes a title, text, media name, review number where applicable
- The user can create an account and log in to the application.
- The user can add previous justified reviews, edit them and delete them.
- The user can see the reviews added to the application and search for reviews with many options, e.g. work, reviewer, year, etc.
- The user page has and can show all reviews and other statistics about users.
- Reviews can be categorized by genre.
- The user can give comments to reviews and comments can link to each other.
- The average value of the work can be searched.

# Checklist
## Basic requirements
### Application requirements
  -  The user can **create an account and log in to the application**.
  -  The user can **add data items to the application**. In addition, the user can edit and delete data items they have added.
  -  The user can **see** the data items added to the application**.
  -  The user can **see** both the data items they have added themselves and those added by other users.
  -  The user can **search for data items by keyword or other criteria**. The user can search for both the data items they have added themselves and those added by other users.
  -  The application has **user pages**, which show statistics for each user and the data items added by the user.
  -  The user can **select one or more classifications for the data item**. Possible categories are in the database.
  -  The application has **in addition to the main data item, a secondary data item**, which supplements the main data item. The user can add secondary data items related to their own and other users' data items.

### Technical requirements
  -  The application was implemented according to the course material.
  -  The application was implemented in Python using the Flask library.
  -  The application uses the SQLite database.
  -  Git and GitHub were used in the development work.
  -  The application's user interface consists of HTML pages.
  -  JavaScript is banned.
  -  The database is used directly with SQL commands (no ORM).
  -  In addition to Flask, no other separately installed Python libraries are used.
  -  The appearance of the application (HTML/CSS) has been implemented by itself without libraries.
  -  The application code is written in English.
  -  The database tables and columns are named in English.

### Version control
  -  `README.md` will document how the application and how to test it.
  -  Commits will be done regularly and in English during development.

### Cybersec
  -  Passwords will be stored in the database properly and according to protocol.
  -  User rights for viewing content within the website will be checked.
  -  User rights to send a form will be checked.
  -  User inputs will be checked before being parsed and sent to the database.
  -  SQL commands will use parameters.
  -  Pages are rendered via page templates (`render_template`).
  -  Forms have a CSRF vulnerability blocked.

### Peer review and returns
  -  First peer review complete.
  -  Second peer review complete.

## Advanced requirements
### UX
  -  The application is easy and logical to use.
  -  The appearance is implemented using CSS.
  -  The Pylint tool was used and the results were reported.
  -  **Line breaks applied by the user is visible in text.**
  -  **Pictures, if present in the app, use `alt` attribute.**
  -  **The form uses `label` elements**
    
### Version control
  -  No extraneous or needless files in version control.
  -  Commits are clean, inform all changes with good messages.
    
### Programming style
  -  Variables and functions named descriptively and clearly.
  -  Use standardised tab length of four spaces.
  -  Code does not have overly long lines
  -  Use `snake_case` for names. No `Title_Case`, no `camelCase`, no `PascalCase`.
  -  Proper spaces around `=` and `,`.
  -  No extraneous parentheses around `if` and `while` structures.
  -  **Used Pylint-tools and reported the results in its own separate file.**
    
### Database style
  -  Tables and columns are named descriptively and clearly.
  -  Use of `REFERENCES` in referral to other tables.
  -  No use of `SELECT *` (Always have a specific column / columns in search named)
  -  Use SQL features in a sensible way.
    
### Peer review and returns
  -  First peer review conducted comprehensively.
  -  Second peer review conducted comprehensively.
  -  Course response given.

### **Large database processing**
  -  The app is tested on larger databases and results are reported.
  -  Pagination of data items used in the application.
  -  Database uses indexes to speed up processing of larger databases.
  -  A suitable way to report the results is to add the `seed.py` file to the repository and write a `README.md` file describing the application's operation with a large amount of information.

# Journal
## 22.3.2026
Currently the files have merely being tested using course material. This is the first time the page will be constructed.
## 25.3.2026
In preparation for implementing the review system, the database has been massively expanded, with missing components and added redundancy. Page for adding those reviews have been prepared but function is not ready.
## 27.3.2026
The login and post system is ... "functional". The database, however, still requires referneces, indexing and other touchups. The decision was made to split up the image implementation of the database into multiple separate tables to enable easy referencing and image implementation into other components of the database.
## 29.3.2026
All base systems are functional. References have been commented out until the implementation can be "locked down". Indexing is functional. SQL injection is no longer an attack vector ... though far more simple attack vectors are possible since these reviews are identified by their id and there is no direct forbid protocol for users manually entering the edit pages of HTML links corresponding to the reviews themselves. This will have to be solved later, as well as many other UX related issues.