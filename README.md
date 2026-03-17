# TikaWe-Projekti-Media-arvostelu
This is a repository for a web application for the University of Helsinki course - Databases and web programming. The programmer is The Dat Vo, nicknamed Michael. The application is a media review, but its structure can be generalized to other applications

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
  -  README.md will document how the application and how to test it.
  -  Commits will be done regularly and in English during development.

### Cybersec
  -  Passwords will be stored in the database properly and according to protocol.
  -  User rights for viewing content within the website will be checked.
  -  User rights to send a form will be checked.
  -  User inputs will be checked before being parsed and sent to the database.
  -  SQL commands will use parameters.
  -  Pages are rendered via page templates (render_template).
  -  Forms have a CSRF vulnerability blocked.

## Advanced requirements
  -  The application is easy and logical to use.
  -  The appearance is implemented using CSS.
  -  The Pylint tool was used and the results were reported.
